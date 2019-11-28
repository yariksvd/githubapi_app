from django.db import models

class ReposModel(models.Model):
    name = models.CharField(null=False, max_length=255)
    html_url = models.CharField(null=False, max_length=1024)
    description = models.TextField(null=True)
    private = models.BooleanField()
    created_at = models.CharField(null=False, max_length=255)
    watchers = models.PositiveIntegerField()

    def __str__(self):
        return self.name