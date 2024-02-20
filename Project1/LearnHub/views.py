from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def home_page(request):
    return render(request,'./index.html')

def player_page(request):
    return render(request,'./player.html')

def course_page(request):
    text = "Fuck you Nigga"
    return render(request, './courses.html',{'text':text})


def print(request):
    a = 2+4
    return HttpResponse(a)