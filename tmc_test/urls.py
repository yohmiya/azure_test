from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_list, name='recommend_list'),
]
