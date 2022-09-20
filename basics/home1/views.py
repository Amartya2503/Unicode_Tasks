from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

#thid code was written to check the server before starting task_3:
# def index(request):
#     # return HttpResponse("welcome to home page")
#     return render(request, 'index.html')

#this function is used to carry out task 3:

def task(request):
    res={ }
    
    if request.method == "POST":
        id= request.POST.get('id')
        
        url = "https://twitter154.p.rapidapi.com/user/id"

        querystring = {"user_id": id}

        headers = {
	         "X-RapidAPI-Key": "cb090dec35mshc902f52340f3319p1db9a8jsn2928a586b761",
	         "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        res=response
        return HttpResponse(res)
           
    return render(request, 'form.html')
#can a view function only return one thng at the time of implimentation ?    