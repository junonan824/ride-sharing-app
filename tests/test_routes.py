import unittest
from app import create_app
from app.models import User
from mongoengine import disconnect

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Clear the test database
        User.objects.delete()

    def tearDown(self):
        self.app_context.pop()
        disconnect()

    def test_create_user(self):
        response = self.client.post('/users', json={
            "userId": "u123",
            "name": "John Doe",
            "location": [40.7128, -74.0060]
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['userId'], "u123")

    def test_get_user(self):
        user = User(userId="u123", name="John Doe", location=[40.7128, -74.0060])
        user.save()
        response = self.client.get('/users/u123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "John Doe")

if __name__ == '__main__':
    unittest.main()