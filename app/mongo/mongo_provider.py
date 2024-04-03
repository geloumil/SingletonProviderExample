import mongoengine

from app.mongo.mongo_models import Student, Teacher


class MongoProvider:
    connected = False

    def __init__(
            self, mongo_db, username, password,
            host, port, authentication_source
    ):
        if not MongoProvider.connected:  # singleton
            mongoengine.connect(
                mongo_db, username,
                password, host,
                port, authentication_source
            )

    @staticmethod
    def get_student(username: str):
        return Student.objects(username=username).first().to_mongo()

    @staticmethod
    def get_students(usernames: list):
        return Student.objects(username__in=usernames).all().to_mongo()

    @staticmethod
    def create_student(username: str):
        student = Student(username=username)
        student.save()
        return student.to_mongo()

    @staticmethod
    def add_teacher(kwargs):
        teacher = Teacher(**kwargs)
        teacher.save()
        return teacher.to_mongo()
