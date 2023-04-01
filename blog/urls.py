from django.urls import path
from blog import views

urlpatterns = [
    path("hello/", views.get_hello, name="hello-view"),
]