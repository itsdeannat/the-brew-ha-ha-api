from django.test import TestCase

# Create your tests here.
class SignupTestCalls(TestCase):
        
    def test_signup_view_valid(self):
        '''
        Tests that a valid data results in successful signup
        '''
        response = self.client.post('/api/signup/', data={
            'username': 'johndoe',
            'password': 'password123',
        }, follow=True)
        self.assertEqual(response.status_code, 201)
        
    def test_signup_view_missing_user_name(self):
        '''
        Tests that missing data results in unsuccessful signup
        '''
        response = self.client.post('/api/signup/', data={
            'username': '',
            'password': 'pass$word123',
        }, follow=True)
        self.assertEqual(response.status_code, 400)
        
    def test_signup_view_bad_data(self):
        '''
        Tests that invalid data results in unsuccessful signup
        '''
        response = self.client.post('/api/signup/', data={
            'username': '$asdk)##$',
            'password': 'pass$worSDFd123',
        }, follow=True)
        self.assertEqual(response.status_code, 400)
        
class JWTAuthenticationCalls(TestCase):
    
    def test_authenticated_user(self):
        '''
        Tests that authenticated user can retrieve JWT
        '''
        user_data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        response = self.client.post('/api/signup/', user_data, format='json')
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/api/token/', user_data, follow=True)
        self.assertEqual(response.status_code, 200)
        
    def test_not_authenticated_user(self):
        '''
        Tests that user can't receive JWT if not authenticated
        '''
        user_data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        response = self.client.post('/api/token/', user_data, follow=True)
        self.assertEqual(response.status_code, 401)
        
class GetAllResourcesCalls(TestCase):
    
    def test_authenticated_get_coffees(self):
        '''
        Tests that an authenticated user can make a GET request to /coffees
        '''
        user_data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        # User signs up for API
        response = self.client.post('/api/signup/', user_data, format='json')
        self.assertEqual(response.status_code, 201)

        # User gets a JWT
        response = self.client.post('/api/token/', user_data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        #Get the JWT from response
        token = response.json().get('access')
        self.assertIsNotNone(token, "Token should be present in the response")
        
        # Send GET request
        response = self.client.get('/api/coffees/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 200)
        
    def test_authenticated_get_snacks(self):
        '''
        Tests that an authenticated user can make a GET request to /snack
        '''
        user_data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        # User signs up for API
        response = self.client.post('/api/signup/', user_data, format='json')
        self.assertEqual(response.status_code, 201)

        # User gets a JWT
        response = self.client.post('/api/token/', user_data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        #Get the JWT from response
        token = response.json().get('access')
        self.assertIsNotNone(token, "Token should be present in the response")
        
        # Send GET request
        response = self.client.get('/api/snacks/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 200)
        
    def test_not_authenticated_get_snacks(self):
        '''
        Tests that an user can't make a GET request if not authenticated
        '''
        user_data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        # User signs up for API
        response = self.client.post('/api/signup/', user_data, format='json')
        self.assertEqual(response.status_code, 201)
        
        #Get the JWT from response
        token = response.json().get('access')
        self.assertIsNone(token, "Token should not be present in the response")
        
        # Send GET request
        response = self.client.get('/api/snacks/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 401)