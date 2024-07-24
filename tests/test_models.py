import unittest
from app.models import User, Trip


class TestModels(unittest.TestCase):

    def test_create_user(self):
        user = User(userId="u123", name="John Doe", location=[40.7128, -74.0060])
        self.assertEqual(user.userId, "u123")
        self.assertEqual(user.name, "John Doe")

    def test_create_trip(self):
        trip = Trip(tripId="t123", driverId="d456", riderId="u123", startLocation=[40.7128, -74.0060],
                    endLocation=[40.730610, -73.935242], status="ongoing", startDate="2024-07-25",
                    endDate="2024-07-25", distance=10.5)
        self.assertEqual(trip.tripId, "t123")


if __name__ == '__main__':
    unittest.main()