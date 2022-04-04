from email import message
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "base_site/home.html", {"user1": request.user})
    

def about(request):
    return HttpResponse("This is an about page")