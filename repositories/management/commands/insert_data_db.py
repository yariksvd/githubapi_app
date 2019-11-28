import requests
import json
import logging
from django.core.management.base import BaseCommand

from repositories.models import ReposModel

logger = logging.getLogger('repository')


REPOSITORIES_ENDPOINT = 'https://api.github.com/users/django/repos'

class Command(BaseCommand):

    def import_repositories(self, data):
        name = data.get('name')
        html_url = data.get('html_url')
        description = data.get('description')
        private = data.get('private')
        created_at = data.get('created_at')
        watchers = data.get('watchers')

        try:
            repository, created = ReposModel.objects.get_or_create(
                name=name,
                html_url=html_url,
                description=description,
                private=private,
                created_at=created_at,
                watchers=watchers
            )
            if created:
                repository.save()
                success_import = f'\nRepository {repository} succesfully inserted\n'
                logger.info(success_import)
            elif not created:
                logger.warning('Duplicate. Recrod already exist\n')
        except Exception as e:
            msg = f'Inserting repository {name} failed\n{str(e)}\n'
            logger.exception(msg)
    
    def handle(self, *args, **options):
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.get(
                url=REPOSITORIES_ENDPOINT,
                headers=headers, 
            )
            response.raise_for_status()
            repos = response.json()
            for repo in repos:
                self.import_repositories(repo)
        except requests.HTTPError as e:
            logger.exception(f'{str(e)}: Wrong repositories endpoint\n')
            