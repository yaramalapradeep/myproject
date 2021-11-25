from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #how are you
    return render(request,'accounts/index')
