from api.class_health_actions import ClassHealthActions
from api.student_health_indicators import StudentHealth
from config.configLoader import ConfigLoader
from config.envLoader import EnvLoader

EnvLoader()
ConfigLoader()

students_to_create = [
    {
        "username": "student1",
        "age": 18
    },
    {
        "username": "student2",
        "fullname": "Student 2",
        "email": "student2@test.com",
        "age": 18
    }
]

for student in students_to_create:
    StudentHealth(student)

teacher = ClassHealthActions("teacher1", [student["username"] for student in students_to_create])
teacher.calculate_class_actions()
# ... pass
