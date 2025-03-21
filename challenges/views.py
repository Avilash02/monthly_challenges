from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def january(request):
    return HttpResponse("This Works!")

def february(request):
    return HttpResponse("This is february")