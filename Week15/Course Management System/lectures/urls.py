from django.conf.urls import url
from lectures import views


urlpatterns = [
    url(r'^new/$', views.new_lecture, name='new_lecture_name'),
    url(r'^edit/(?P<lecture_id>[0-9]+)/$', views.edit_lecture, name='edit_lecture_name'),
    url(r'^(?P<lecture_id>[0-9]+)/$', views.display_lecture, name='display_lecture_name')
]
