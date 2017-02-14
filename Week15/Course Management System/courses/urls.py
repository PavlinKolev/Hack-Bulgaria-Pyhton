from django.conf.urls import url
import courses.views as views


urlpatterns = [
    url(r'^$', views.courses_table, name="table_courses_name"),
    url(r'^course/new/$', views.new_course, name="new_course_name"),
    url(r'^course/(?P<course_name>[+-?!A-za-z0-9]+)/$', views.display_couse, name="display_course"),
    url(r'^course/edit/(?P<course_name>[+-?!A-za-z0-9]+)/$', views.edit_course, name="edit_course")
]
