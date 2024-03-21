# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Здесь же была ракета!</h1>')
