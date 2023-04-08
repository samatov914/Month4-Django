from django.test import TestCase, Client
from django.urls import reverse



class BlogViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("index-page"))
        self.assertTemplateUsed(response,"blog/index.html")
        self.assertEqual(200, response.status_code)
        

    def test_about(self):
        response = self.client.get(reverse("about-view"))
        self.assertTemplateUsed(response,"blog/about.html")
        self.assertEqual(200, response.status_code)

    def test_contact(self):
        response = self.client.get(reverse("contact-view"))
        self.assertTemplateUsed(response,"blog/contact.html")
        self.assertEqual(200, response.status_code)