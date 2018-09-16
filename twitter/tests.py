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

    def test_signup_and_login(self):
        c = Client()
        credentials = {
                'username':'test123',
                'password1':'P@ssw0rd1',
                'password2':'P@ssw0rd1',
                };
        response = c.post(reverse('twitter:signup'), credentials)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('twitter:home'))

    def test_logout(self):
        c = Client()
        credentials = {
                'username':'test123',
                'password1':'P@ssw0rd1',
                'password2':'P@ssw0rd1',
                };
        response = c.post(reverse('twitter:signup'), credentials)
        response = c.post(reverse('twitter:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('twitter:index'))

    def test_login(self):
        c = Client()
        signup_credentials = {
                'username':'test123',
                'password1':'P@ssw0rd1',
                'password2':'P@ssw0rd1',
                };
        response = c.post(reverse('twitter:signup'), signup_credentials)
        response = c.post(reverse('twitter:logout'))
        login_credentials = {
                'username':'test123',
                'password':'P@ssw0rd1',
                };
        response = c.post(reverse('twitter:login'), login_credentials)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('twitter:home'))


