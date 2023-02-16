from django.shortcuts import render
from blog.models import Post


def index(request):
    posts = Post.objects.all()
    try:
        posts = posts[0:3]
    except IndexError:
        pass
    return render(request, 'index.html', {"posts": posts})