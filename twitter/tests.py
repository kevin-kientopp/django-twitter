from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        """When an unauthenticed user visits the index, the index page is rendered."""
        response = self.client.get(reverse('twitter:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to my Twitter clone!')
        self.assertContains(response, 'Sign up')
        self.assertContains(response, 'Log in')

    def test_signup(self):
        creds = create_signup_creds();
        response = self.client.post(reverse('twitter:signup'), creds)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('twitter:home'))

    def test_logout(self):
        creds = create_signup_creds();
        response = self.client.post(reverse('twitter:signup'), creds)
        response = self.client.post(reverse('twitter:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('twitter:index'))

    def test_login(self):
        signup_creds = create_signup_creds();
        response = self.client.post(reverse('twitter:signup'), signup_creds)
        response = self.client.post(reverse('twitter:logout'))
        login_creds = {
                'username':'test123',
                'password':'P@ssw0rd1',
                };
        response = self.client.post(reverse('twitter:login'), login_creds)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('twitter:home'))

    def test_tweet(self):
        creds = create_signup_creds();
        response = self.client.post(reverse('twitter:signup'), creds)
        tweet = {
                'body': 'This is a test...'
                };
        response = self.client.post(reverse('twitter:home'), tweet)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('twitter:home'))

def create_signup_creds():
    return {
            'username':'test123',
            'password1':'P@ssw0rd1',
            'password2':'P@ssw0rd1',
            };
