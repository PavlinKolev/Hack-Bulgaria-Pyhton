from django.shortcuts import render
from django.shortcuts import get_object_or_404
from lectures.models import Lecture
from lectures.forms import LectureForm


def new_lecture(request):
    form = LectureForm()
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'new_lecture.html', locals())


def edit_lecture(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    form = LectureForm(initial=lecture.get_dict())
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save_lecture(lecture)
    return render(request, 'edit_lecture.html', locals())


def display_lecture(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    return render(request, 'display_lecture.html', locals())
