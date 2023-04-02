from django.urls import path
from blog import views

urlpatterns = [
    path("hello/", views.get_hello, name="hello-view"),
    path("contacts/", views.get_contacts, name="contacts-view"),
    path("about/", views.get_about, name="about-view"),
]