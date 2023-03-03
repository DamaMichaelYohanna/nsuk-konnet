from django.urls import path
from . import views
urlpatterns =[
    path("", views.index, name='home page'),
    path("about", views.about_us, name='about us'),
    path("past-questions", views.pass_questions, name='about us'),
]