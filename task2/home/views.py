from cgitb import html
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from task2 import task_1

# Create your views here.
# def task(request, range, range2):
    
#     x= task_1.my_task(range, range2)
#     return HttpResponse(x)

def task(request, range1, range2):
    x= task_1.my_task(range1, range2)
    context={
        'variable1': x[0],
        'variable2' : x[1]
    }
    return render(request, 'view.html' , context)


  #tested dynamic urs with this functrion:  
def index(request, demand):
    if demand == 'about':
        return HttpResponse('this is the about page')

        