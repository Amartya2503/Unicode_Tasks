from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('<demand>', views.index, name='home'),
    path('<int:range1>/<int:range2>', views.task, name='input')
   
    
]