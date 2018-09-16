from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class ViewsTestCase(TestCase):
    def test_index(self):
        """When an unauthenticed user visits the index, the index page is rendered."""
        c = Client()
        response = c.get(reverse('twitter:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to my Twitter clone!')
        self.assertContains(response, 'Sign up')
        self.assertContains(response, 'Log in')

