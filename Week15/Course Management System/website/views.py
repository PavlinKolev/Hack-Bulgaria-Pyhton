from django.shortcuts import render
from courses.models import Course


def courses_table(request):
    all_courses = Course.objects.all()
    return render(request, "all_courses.html", locals())
