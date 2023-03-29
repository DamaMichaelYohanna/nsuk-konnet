from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about_us, name='about us'),
    path("past-questions", views.pass_questions, name='about us'),
    #     -----------------------------------
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
]
