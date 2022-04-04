from email import message
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "main/home.html", {"user": request.user})
    

def about(request):
    return HttpResponse("This is an about page")