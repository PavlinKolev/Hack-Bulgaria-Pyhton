from django.db import models
from courses.models import Course


class Lecture(models.Model):
    name = models.CharField(max_length=30, unique=True)
    week = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, blank=True, null=True)
    url = models.CharField(max_length=120)

    def set_name(self, name):
        self.name = name

    def set_week(self, week):
        self.week = week

    def set_course(self, course):
        self.course = course

    def set_url(self, url):
        self.url = url
