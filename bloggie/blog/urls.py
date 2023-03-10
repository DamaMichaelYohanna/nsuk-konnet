from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path("", views.BlogList.as_view(), name='post_list'),
    path("<slug:slug>/", views.BlogView.as_view(), name='post_detail'),
    path('search', views.SearchView.as_view(), name='search'),
]