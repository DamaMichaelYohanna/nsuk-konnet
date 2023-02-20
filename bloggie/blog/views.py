from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView


from .models import Post, Comment
from .forms import CommentForm


class BlogList(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'post_list.html'
    context_object_name = 'post_list'


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
        context ={'post_detail': post, 'more_post': more_post, 'popular_post': more_post}
        return render(request, 'post_detail.html', context)


