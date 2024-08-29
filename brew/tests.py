from django.test import TestCase

# Create your tests here.
class RegistrationTestCalls(TestCase):
        
    def test_registration_view_valid(self):
        response = self.client.post('/register/', data={
            'username': 'johndoe',
            'password': 'password123',
        }, follow=True)
        self.assertEqual(response.status_code, 201)
        
    def test_registration_view_missing_user_name(self):
        response = self.client.post('/register/', data={
            'username': '',
            'password': 'pass$word123',
        }, follow=True)
        self.assertEqual(response.status_code, 400)
        
    def test_registration_view_bad_data(self):
        response = self.client.post('/register/', data={
            'username': '$asdk)##$',
            'password': 'pass$worSDFd123',
        }, follow=True)
        self.assertEqual(response.status_code, 400)