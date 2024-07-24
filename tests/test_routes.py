import unittest
from app import create_app
from app.models import User


class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/users', json={
            "userId": "u123",
            "name": "John Doe",
            "location": [40.7128, -74.0060]
        })
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        user = User(userId="u123", name="John Doe", location=[40.7128, -74.0060])
        user.save()
        response = self.client.get('/users/u123')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()