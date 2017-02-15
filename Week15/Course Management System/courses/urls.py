from django.conf.urls import url
from courses import views


urlpatterns = [
    url(r'^new/$', views.new_course, name="new_course_name"),
    url(r'^(?P<course_name>[% +-?!A-za-z0-9]+)/$', views.display_course, name="display_course"),
    url(r'^edit/(?P<course_name>[% +-?!A-za-z0-9]+)/$', views.edit_course, name="edit_course")
]
