from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wish(request):
    return HttpResponse("<h1>Welcome to django</h1>")
def display(request):
    return HttpResponse("<h1>We are in display method</h1>")

def m1(request):
    return render(request,'first.html')