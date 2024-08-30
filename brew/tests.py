from django.test import TestCase

# Create your tests here.
class RegistrationTestCalls(TestCase):
        
    def test_registration_view_valid(self):
        '''
        Tests that a valid data results in successful registration
        '''
        response = self.client.post('/register/', data={
            'username': 'johndoe',
            'password': 'password123',
        }, follow=True)
        self.assertEqual(response.status_code, 201)
        
    def test_registration_view_missing_user_name(self):
        '''
        Tests that missing data results in unsuccessful registration
        '''
        response = self.client.post('/register/', data={
            'username': '',
            'password': 'pass$word123',
        }, follow=True)
        self.assertEqual(response.status_code, 400)
        
    def test_registration_view_bad_data(self):
        '''
        Tests that invalid data results in unsuccessful registration
        '''
        response = self.client.post('/register/', data={
            'username': '$asdk)##$',
            'password': 'pass$worSDFd123',
        }, follow=True)
        self.assertEqual(response.status_code, 400)
        
class JWTAuthenticationCalls(TestCase):
    
    def test_registered_user(self):
        '''
        Tests that registered user can retrieve JWT
        '''
        user_data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        response = self.client.post('/register/', user_data, format='json')
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/api/token/', user_data, follow=True)
        self.assertEqual(response.status_code, 200)
        
    def test_unregistered_user(self):
        '''
        Tests that unregistered user can't receive JWT
        '''
        user_data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        response = self.client.post('/api/token/', user_data, follow=True)
        self.assertEqual(response.status_code, 401)