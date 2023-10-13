from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("index page")

def index(request):
    # Displays exclusively the parameter being pointed.
    return render(request, "hello/index.html")

# def greet(request, text):
#     return HttpResponse(f"Greetings {text.capitalize()}")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })