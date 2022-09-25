from multiprocessing import context
from typing import Counter
from django.shortcuts import render, HttpResponse
import requests
from .models import details
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#thid code was written to check the server before starting task_3:
# def index(request):
#     # return HttpResponse("welcome to home page")
#     return render(request, 'index.html')

#this function is used to carry out task 3:

def task_3(request):
    
    
    if request.method == "POST":
        #try except used to avoid getting error page in case we get error page we print user not found
        
        try:

           #storing the recieved input from form in variable id 
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

                detail= details(Username = user_name, Userid= id , Counter=0)
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

            User = details.objects.get(Userid = id)
            
            context = {
                'variable1' : id,
                'variable2' : User
            }
            
            print(User.Counter) 
            User.Counter += 1
            User.save()    
                                           
            return render(request, 'Querry.html', context)
      #this except takes care if get can not find the data in the data base
        except ObjectDoesNotExist:

            context={
                'variable1' : id,
                'variable2' : "User Not Found "
            }
            return render(request, 'Querry.html', context)
            
            
      #this exception block takes care of invalid inputs such as alphabets or blank spaces

        except ValueError:
            context={
                'variable1' : "please enter a valid input",
                'variable2' : " "
            }
            return render(request, 'Querry.html', context)
            

    else :
        return render(request, 'Querry.html')

#now we create a view to display top 3 entries from database

def top_3(request):
    x= { }
    users= details.objects.all().order_by('-Counter')
    
    print(users)
    for i in users:
        C_ount=details.objects.get(Username= i)
        # print(C_ount.Counter)
       
        x[i.Username] = C_ount.Counter
     
    context={
        'var':x
        }
    return render(request, 'top3.html', context)
    

