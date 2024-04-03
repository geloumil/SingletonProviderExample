from mongoengine import Document, StringField, EmailField, BooleanField, DynamicDocument, IntField, LazyReferenceField, \
    ListField


class Student(Document):
    username = StringField(required=True, primary_key=True)
    fullname = StringField(required=False)
    email = EmailField(required=False, default=None)
    active = BooleanField(required=False, default=True)
    enabled = BooleanField(default=True)
    age = IntField(required=False, default=None)


class Teacher(DynamicDocument):
    username = StringField(required=True, primary_key=True)
    fullname = StringField(required=False)
    email = EmailField(required=False, default=None)
    active = BooleanField(required=False, default=True)
    enabled = BooleanField(default=True)
    students = ListField(LazyReferenceField(Student), default=[])
