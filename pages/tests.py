from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):

    def test_hompage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def  test_aboutpage(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code,200)
