from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# get_about/ -> "About"
# get_contacts/ -> 

def hello(request):
    heading = """<h1> Закголовок 1 lvl</h1>
    <h2> Загаловок 2 lvl
    """

    return HttpResponse("Hello", headers={"Name": "Alex"}, status = 500)
    # return HttpResponse(heading)
