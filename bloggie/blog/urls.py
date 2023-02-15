from django.urls import path

from . import views

urlpatterns = [
    path("", views.BlogList.as_view(), name='blog list'),
    path("<slug:slug>/", views.BlogView.as_view(), name='blog_list'),
    # path("comment/", views.PostComment.as_view(), name="post comment"),
]