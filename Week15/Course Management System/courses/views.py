from django.shortcuts import render
from django.shortcuts import get_object_or_404
from courses.models import Course


def courses_table(request):
    all_courses = Course.objects.all()
    return render(request, "course_table.html", locals())


def display_couse(request, course_name):
    import ipdb; ipdb.set_trace()
    # course = Course.objects.get(name=course_name)
    course = get_object_or_404(Course, name=course_name)
    return render(request, "course.html", locals())


def new_course(request):
    # import ipdb; ipdb.set_trace()
    if request.method == "POST":
        name = request.POST.get('name')
        descr = request.POST.get('descr')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        course = Course.objects.create(name=name, descr=descr, start_date=start_date, end_date=end_date)
    return render(request, "new_course.html", locals())


def edit_course(request, course_name):
    # import ipdb; ipdb.set_trace()
    course = get_object_or_404(Course, name=course_name)
    if request.method == "POST":
        course.set_name(request.POST.get('name'))
        course.set_descr(request.POST.get('descr'))
        course.set_start_date(request.POST.get('start_date'))
        course.set_end_date(request.POST.get('end_date'))
        course.save()
    start_date = "{}-{:02d}-{:02d}".format(course.start_date.year, course.start_date.month, course.start_date.day)
    end_date = "{}-{:02d}-{:02d}".format(course.end_date.year, course.end_date.month, course.end_date.day)
    return render(request, "edit_course.html", locals())
