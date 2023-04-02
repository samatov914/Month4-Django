from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# get_about/ -> "About"
# get_contacts/ -> 

def hello(request):
    heading = """<h1> Заголовок 1 lvl</h1>
    <h2> Загаловок 2 lvl
    
    """

    return HttpResponse("Hello", headers={"Name": "Alex"}, status = 200)
    # return HttpResponse(heading)

def get_contact(request):
    return HttpResponse("Number",headers={"Name": "Alex"}, status = 200)

def get_about(request):
    return HttpResponse("about",headers={"Name": "Alex"}, status = 200)