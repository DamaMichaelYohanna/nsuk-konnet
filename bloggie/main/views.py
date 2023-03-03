from django.shortcuts import render
from blog.models import Post


def index(request):
    posts = Post.objects.all()
    try:
        posts = posts[0:3]
    except IndexError:
        pass
    return render(request, 'index.html', {"posts": posts})


def about_us(request):
    return render(request, 'about.html',)


def pass_questions(request):
    return render(request, 'pass_questions.html')