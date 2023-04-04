from django.shortcuts import render
from django.http import HttpResponse

# get_about(request) - about/ -> "About"
# get_contacts(request) - contacts/ -> "Contacts"
def get_hello(request):
    # request -> Объект класса HttpRequest, который формируется из запроса от клиента на наш сервер
    # my_list = [1, 2, 3]
    #     heading = """<!DOCTYPE html>
    # <html lang="ru">
    # <head>
    #   <meta charset="UTF-8">
    #   <title>Базовая разметка HTML</title>
    # </head>
    # <body>
    #   <h1>Code Basics</h1>
    #   <p>Бесплатные уроки по программированию и HTML для новичков</p>
    # </body>
    # </html>
    #                  """

    return HttpResponse("Hello", headers={"Name": "Alex"}, status=200)

def get_contacts(request):
    return HttpResponse("number")

def get_about(request):
    return HttpResponse("about")