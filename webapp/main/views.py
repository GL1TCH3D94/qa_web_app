from email import message
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, "main/home.html", {"user": request.user})
    

def about_view(request):
    return HttpResponse("This is an about page")