from django.http import HttpResponse
from django.shortcuts import render

# Create your view logic here
def index(request):
  return render(request, "HELLO/index.html")

# def gauri(request):
#   return HttpResponse("Hello, Gauri")

# now this makes the url path dynamic 
def greet(request, name): 
  return render(request, "HELLO/greet.html", {
    "name": name.capitalize()
  })