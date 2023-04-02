from django.urls import path
from blog import views

urlpatterns = [
    path("hello/", views.get_hello, name="hello-view"),
    path("contact/", views.get_contact, name="contact-view"),
    path("about/", views.get_about, name="about-view"),
]