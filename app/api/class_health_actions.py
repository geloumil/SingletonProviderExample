from typing import List
from mongo.mongo_provider import MongoProvider


class ClassHealthActions:

    def __init__(self, teacher: str, students: List[str]):
        self.username = teacher
        MongoProvider.add_teacher(teacher)
        self.students = MongoProvider.get_students(students)

    def calculate_class_actions(self):
        pass
