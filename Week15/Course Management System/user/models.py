from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def is_lecturer(self):
        return self.__class__.__name__ == "Lecturer"


class Student(User):
    pass


class Lecturer(User):
    pass
