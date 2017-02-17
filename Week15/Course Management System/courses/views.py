from django.shortcuts import render
from django.shortcuts import get_object_or_404
from courses.models import Course
from lectures.models import Lecture
from courses.forms import CourseForm


def display_course(request, course_name):
    course = get_object_or_404(Course, name=course_name)
    lectures = Lecture.objects.filter(course=course)
    return render(request, "course.html", locals())


def new_course(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "new_course.html", locals())


def edit_course(request, course_name):
    course = get_object_or_404(Course, name=course_name)
    form = CourseForm(initial=course.get_dict())
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save_course(course)
    return render(request, "edit_course.html", locals())
