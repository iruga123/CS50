from django import forms
from django.shortcuts import render
from django.http import *
from django.urls import *
# import datetime

assigned_to = [('namone', 'Namone'),
               ('namtwo', 'Namtwo'),
               ('namthree', 'Namthree')]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # assigned_to = forms.CharField(label="Assigned", widget=forms.Select(choices = assigned_to))

# Create your views here.
def index(request):
    # now = datetime.datetime.now()
    if "tasks" not in request.session:
        request.session["tasks"] = []       
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    
def add(request):
    # Validates and cleanses the data submitted through form
    if request.method =="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
           
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })