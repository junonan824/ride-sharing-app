# RideNow - Real-Time Ride-Sharing Application

RideNow is a real-time ride-sharing application built with MongoDB and Python. This application is designed to handle user data, trip data, and geolocation data for drivers and riders.

## Features

- Create, read, update, and delete users and trips
- Geospatial queries to find nearby drivers
- Aggregation to calculate average trip distances
- Real-time updates for ride status

## File Structure

ride-sharing-app/
│
├── app/
│   ├── init.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   └── utils.py
│
├── tests/
│   ├── init.py
│   ├── test_models.py
│   ├── test_routes.py
│   ├── test_services.py
│
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── app.py

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/ride-sharing-app.git
    cd ride-sharing-app
    ```

2. Create a virtual environment and install dependencies
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the application
    ```bash
    python app.py
    ```

## Running Tests

To run the tests, use:
```bash
pytest

API Endpoints

Users

	•	POST /users: Create a new user
	•	GET /users/<userId>: Get user details
	•	PUT /users/<userId>: Update user details
	•	DELETE /users/<userId>: Delete a user

Trips

	•	POST /trips: Create a new trip
	•	GET /trips/date-range: Get trips within a date range
	•	GET /trips/average-distance: Get average trip distance per driver
	•	GET /drivers/nearby: Get nearby drivers

## Conclusion

Thank you for using our ride-sharing app! We hope it meets your needs and provides a seamless experience. If you have any feedback, suggestions, or issues, please feel free to open an issue on our GitHub repository.

Happy riding!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

