from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name = 'index'),
    path('search/', views.SearchResults, name = 'search_results'),
              
]