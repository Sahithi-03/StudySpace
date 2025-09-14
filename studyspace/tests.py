from django.test import TestCase
from .models import *
from django.test import Client, TestCase
# Create your tests here.

class StudyspaceTestCase(TestCase):

    def test_index(self):

        # Set up client to make requests
        c = Client()

        # Send get request to index page and store response
        response = c.get("//")

        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    StudyspaceTestCase()


