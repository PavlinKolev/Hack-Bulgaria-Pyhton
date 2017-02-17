from django import forms
from courses.models import Course


class CourseForm(forms.Form):
    name = forms.CharField(max_length=30)
    descr = forms.CharField(required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def save(self, commit=True):
        course = Course.objects.create(name=self.cleaned_data['name'],
                                    descr=self.cleaned_data['descr'],
                                    start_date=self.cleaned_data['start_date'],
                                    end_date=self.cleaned_data['end_date'])
        return course

    def save_course(self, course):
        for k, v in self.cleaned_data.items():
            if v:
                course.set(k, v)
        course.save()
        return course
