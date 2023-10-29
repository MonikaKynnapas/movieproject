from django.urls import path
from . import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('search_result/', views.SearchResultView.as_view(), name='search_result'),
]