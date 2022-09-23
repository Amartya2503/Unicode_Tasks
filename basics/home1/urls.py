from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('form/',views.task_3, name = 'task_3,4'),
    path('querry/', views.querry, name = 'task_4')
] 
