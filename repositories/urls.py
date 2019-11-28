from django.urls import path

from .views import RepositoriesListView, RepositoryDetailView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('repos_list/', RepositoriesListView.as_view(), name='repos_list'),
    path('detail_repo/<int:pk>/', RepositoryDetailView.as_view(), name='detail_repo'),
]