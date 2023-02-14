from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment


class BlogList(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'post_list.html'
    context_object_name = 'post_list'


class BlogView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['more_post'] = Post.objects.all()[:2]
        return context


class PostComment(CreateView):
    model = Comment
    def post(self, request, *args, **kwargs):

