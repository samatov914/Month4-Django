from django.test import TestCase, Client
from django.urls import reverse


class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-view"))
        expected_data = "Hello"
        self.assertEqual(expected_data, response.content.decode())
        self.assertEqual(500, response.status_code)
           
class ContactsViewTestCase(TestCase):
    def setup(self):
        self.client = Client()
    
    def test_contacts(self):
        response = self.client.get(reverse('contact-view'))
        excepted_data = 'Number'
        self.assertEqual(excepted_data, response.content.decode())

class AboutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about(self):
        response = self.client.get(reverse('about-view'))
        excepted_data = "about"
        self.assertEqual(excepted_data, response.content.decode())
