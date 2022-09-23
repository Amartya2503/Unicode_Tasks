from multiprocessing import context
from django.shortcuts import render, HttpResponse
import requests
from .models import details
# Create your views here.

#thid code was written to check the server before starting task_3:
# def index(request):
#     # return HttpResponse("welcome to home page")
#     return render(request, 'index.html')

#this function is used to carry out task 3:

def task_3(request):
    
    
    if request.method == "POST":

        #storing the recieved input from form in variable id

        id= request.POST.get('id')
        
        url = "https://twitter154.p.rapidapi.com/user/id"

        #passing the variable to querrystring

        querystring = {"user_id": id}

        headers = {
	         "X-RapidAPI-Key": "cb090dec35mshc902f52340f3319p1db9a8jsn2928a586b761",
	         "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        user_name= response['username'] 
        userid= response['user_id']
        context = {
            'variable1' : id,
            'variable2' : user_name
        }

        #sending the data to database
        detail= details(Username = user_name, Userid= id)
        detail.save()

        return render(request, 'form.html', context)
        
           
    return render(request, 'form.html')
#can a view function only return one thng at the time of implimentation ?    

#view for qurrying database using user input:
def querry(request):

    if request.method == "POST":
        id = request.POST.get('id')
        try:

            U_name = details.objects.filter(Userid= id)
            context = {
                'variable1' : id,
                'variable2' : U_name[0]
            }
        
            return render(request, 'Querry.html', context)

        except IndexError:
            context={
                'variable1' : id,
                'variable2' : "User Not Found"
            }
            return render(request, 'Querry.html', context)

    else :
        return render(request, 'Querry.html')
        