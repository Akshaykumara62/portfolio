from django.shortcuts import render
from django.http import HttpResponse, request

def home(request):
    return render(request,'home.html')
# Create your views here.
