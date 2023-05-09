from django.urls import  path

from . import  views


urlpatterns =[
    path("course/list", views.course_list, name="course list"),

]