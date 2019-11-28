from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import ReposModel

# Create your views here.
class RepositoriesListView(ListView):
    model = ReposModel
    context_object_name = 'repositories'
    template_name = 'list_repos.html'


class RepositoryDetailView(DetailView):
    model = ReposModel
    context_object_name = 'repository'
    template_name = 'detail_repo.html'

class HomePageView(TemplateView):
    template_name = 'home.html'
