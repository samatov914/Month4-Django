# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_hello(request):
    return  HttpResponse("Hello", headers={"name": "alex"}, status=500)

def get_contacts(request):
    return HttpResponse("number")

def get_about(request):
    return HttpResponse("about")