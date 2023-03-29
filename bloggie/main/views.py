from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from blog.models import Post


def login_view(request):
    """custom login for user"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username, password)
        if user and user.is_active:
            login(request, user)
            if user.store:
                return redirect("/market/store")
            elif user.catalog:
                return redirect("/market/catalog")

    return render(request, "main/login.html")


def index(request):
    posts = Post.objects.all()
    try:
        posts = posts[0:3]
    except IndexError:
        pass
    return render(request, 'index.html', {"posts": posts})


def about_us(request):
    return render(request, 'about.html', )


def pass_questions(request):
    return render(request, 'pass_questions.html')
