from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

#thid code was written to check the server before starting task_3:
# def index(request):
#     # return HttpResponse("welcome to home page")
#     return render(request, 'index.html')

#this function is used to carry out task 3:

def task(request):
    res=[]
    
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
        # user_name= res['username']
        # userid= res['user_id']
        res=["user name:",user_name," |user id:",userid]
        return HttpResponse(res) 
           
    return render(request, 'form.html')
#can a view function only return one thng at the time of implimentation ?    