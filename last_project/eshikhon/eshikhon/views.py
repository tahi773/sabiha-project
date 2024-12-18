from django.http import HttpResponse
from django.shortcuts import render
  
def home(request):
    return HttpResponse("welcome to eshikhon.")  
def login(request):
    return HttpResponse("welcome to login page.")  
      