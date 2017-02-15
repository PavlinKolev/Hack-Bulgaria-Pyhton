from django.shortcuts import render
from django.shortcuts import get_object_or_404
from lectures.models import Lecture
from courses.models import Course


def new_lecture(request):
    all_courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        weeks = request.POST.get('week')
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        url = request.POST.get('url')
        Lecture.objects.create(name=name, week=weeks, course=course, url=url)
    return render(request, 'new_lecture.html', locals())


def edit_lecture(request, lecture_id):
    all_courses = Course.objects.all()
    lecture = get_object_or_404(Lecture, id=lecture_id)
    if request.method == 'POST' and request.POST.get('edit'):
        lecture.set_name(request.POST.get('name'))
        lecture.set_week(request.POST.get('week'))
        course_id = request.POST.get('course_id')
        lecture.set_course(Course.objects.get(id=course_id))
        lecture.set_url(request.POST.get('url'))
        lecture.save()
    return render(request, 'edit_lecture.html', locals())


def display_lecture(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    return render(request, 'display_lecture.html', locals())
