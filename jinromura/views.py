from django.shortcuts import render
from django.http import HttpResponse
from .models import Village,Character

# Create your views here.
def index(request):
    return HttpResponse("Hello world.")

def detail(request):
    return HttpResponse("Hello world.")
