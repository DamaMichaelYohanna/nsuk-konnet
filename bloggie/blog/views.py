from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm


class BlogList(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    paginate_by = 15


class BlogView(CreateView):
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            print("form is not valid")
        messages.success(request, "Comment Submitted successfuly")
        return redirect(f"/blog/{kwargs['slug']}")

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        more_post = Post.objects.all()[:2]
        context = {'post_detail': post, 'more_post': more_post, 'popular_post': more_post}
        return render(request, 'post_detail.html', context)


class SearchView(ListView):
    """Search Functionality for Blog post"""
    model = Post
    template_name = 'search.html'
    context_object_name = 'search_result'

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        search_key = self.request.GET.get('search')
        if search_key:
            return queryset.filter(title__icontains=search_key)
        else:
            return None
