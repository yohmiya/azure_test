from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_list, name='recommend_list'),
    path('search_list/', views.recommend_search_list, name='recommend_search_list'),
]
