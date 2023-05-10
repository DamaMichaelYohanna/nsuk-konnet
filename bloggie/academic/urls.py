from django.urls import  path

from . import  views


urlpatterns =[
    path("course/list", views.course_list, name="course list"),
    path('ajax/load-cities/', views.load_department, name='ajax_load_dept'),

]