import pytest
from app import create_app
from mongoengine import disconnect, connect


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_name='testing')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

    disconnect()


@pytest.fixture(scope='module')
def init_database():
    # Connect to the test database
    connect('rideNow_test', host='localhost', port=27017)

    # Ensure a clean database before each test
    from app.models import User, Trip
    User.drop_collection()
    Trip.drop_collection()

    yield

    # Cleanup the test database after each test
    User.drop_collection()
    Trip.drop_collection()
    disconnect()