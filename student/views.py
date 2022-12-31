from django.shortcuts import render
from django.http import HttpResponse # DEFAULT OLARAK VAR

# Create your views here.

def home(request):
    return HttpResponse("Hello Django")