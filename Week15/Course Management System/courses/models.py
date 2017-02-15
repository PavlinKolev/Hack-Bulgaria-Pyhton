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
        if end_date and end_date < date:
            raise ValueError("Start date for course cannot be after end date.")
        self.start_date = date

    def set_end_date(self, end_date):
        date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        if start_date and start_date > date:
            raise ValueError("End date for course cannot be before start date.")
        self.end_date = date

    def get_duration(self):
        months = ((self.end_date - self.start_date).days)//30
        if months < 1:
            return "Less than a month"
        return "{} months".format(months)
