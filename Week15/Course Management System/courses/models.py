from django.db import models
import datetime


class Course(models.Model):
    name = models.CharField(max_length=30)
    descr = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def set_name(self, name):
        self.name = name

    def set_descr(self, descr):
        self.descr = descr

    def set_start_date(self, start_date):
        date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.start_date = date

    def set_end_date(self, end_date):
        date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        self.end_date = date
