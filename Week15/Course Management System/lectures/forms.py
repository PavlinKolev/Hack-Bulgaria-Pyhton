from django import forms
from lectures.models import Lecture
from courses.models import Course

OPTIONS = tuple([(course.id, course.name) for course in Course.objects.all()])


class LectureForm(forms.Form):
    name = forms.CharField(max_length=30, required=False)
    week = forms.IntegerField(required=False)
    course = forms.ChoiceField(choices=OPTIONS, widget=forms.Select(), required=False)
    url = forms.CharField(max_length=120, required=False)

    def clean_course(self):
        return Course.objects.get(id=self.cleaned_data['course'])

    def save(self, commit=True):
        lecture = Lecture.objects.create(name=self.cleaned_data['name'],
                                        week=self.cleaned_data['week'],
                                        course=self.cleaned_data['course'],
                                        url=self.cleaned_data['url'])
        return lecture

    def save_lecture(self, lecture):
        for k, v in self.cleaned_data.items():
            if v:
                lecture.set(k, v)
        lecture.save()
        return lecture
