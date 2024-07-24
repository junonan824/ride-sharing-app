from mongoengine import Document, StringField, PointField, DateTimeField, FloatField


class User(Document):
    userId = StringField(required=True, unique=True)
    name = StringField(required=True)
    location = PointField(required=True)


class Trip(Document):
    tripId = StringField(required=True, unique=True)
    driverId = StringField(required=True)
    riderId = StringField(required=True)
    startLocation = PointField(required=True)
    endLocation = PointField(required=True)
    status = StringField(required=True)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)
    distance = FloatField(required=True)
