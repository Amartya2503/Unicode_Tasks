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
        #try except used to avoid getting error page in case we get error page we print user not found
        #storing the recieved input from form in variable id
        try:
            
            id= request.POST.get('id')
        
            url = "https://twitter154.p.rapidapi.com/user/id"

            #passing the variable to querrystring

            querystring = {"user_id": id}

            headers = {
	            "X-RapidAPI-Key": "14e110ca3cmsh4c44c7fb60b8f0bp1e963cjsn869c8b704bc3",
	            "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
            }


            response = requests.request("GET", url, headers=headers, params=querystring).json()
            user_name= response['username'] 
            userid= response['user_id']
            try:
            
                details.objects.filter(Username= user_name).get()

                context = {
                    'variable1' : id,
                    'variable2' : user_name
                }
                return render(request, 'form.html', context)
            except:

            

                context = {
                    'variable1' : id,
                    'variable2' : user_name
                }

                #sending the data to database

                detail= details(Username = user_name, Userid= id)
                detail.save()

                return render(request, 'form.html', context)
        except KeyError:

            context = {
                    'variable1' : id,
                    'variable2' : "User not found"
                }
            return render(request, 'form.html', context)
    else:
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
        