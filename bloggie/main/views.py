from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, reverse
from blog.models import Post


def login_view(request):
    """custom login for user"""
    error = False
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            if user.store:
                return redirect("/market/store")
            elif user.catalog:
                return redirect("/market/catalog")
        else:
            error = True

    return render(request, "login.html", {'error': error})


def logout_view(request):
    logout(request)
    return redirect(reverse("main:home"))


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

