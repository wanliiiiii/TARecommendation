from django.shortcuts import render
from models import User,TravelInfo
from django.http import HttpResponse

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')


