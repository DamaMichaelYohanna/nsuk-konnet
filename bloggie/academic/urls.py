from django.urls import  path

from . import  views


urlpatterns = [
    path("course/list", views.course_list, name="course list"),
    path('ajax/load-cities/', views.load_department, name='ajax_load_dept'),
    path("orientation/", views.orientation, name="orientation"),
    path("past-question/", views.past_question, name="pass questions"),
    path("cbt/", views.cbt, name="cbt")

]