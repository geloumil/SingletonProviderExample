from mongo.mongo_provider import MongoProvider


class StudentHealth:

    def __init__(self, kwargs):
        self.username = kwargs["username"]
        MongoProvider.create_student(kwargs)

    def calculate_health_status(self):
        student_data = MongoProvider.get_student(self.username)
        # Calculating + returning health status
        pass
