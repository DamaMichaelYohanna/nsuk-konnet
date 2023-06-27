from django.contrib.auth import login, logout, authenticate, get_user_model
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
            # if user.store:
            return redirect("/")
            # elif user.catalog:
            # return redirect("/market/catalog")
        else:
            error = True

    return render(request, "login.html", {'error': error})


def logout_view(request):
    logout(request)
    return redirect(reverse("main:home"))


def register_view(request):
    """register view for user"""
    error = False
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if username and password2 == password:
            new_user = get_user_model().objects.create(username=username)
            new_user.set_password(password)
            new_user.save()
            return redirect("/login")
        else:
            error = True

    return render(request, "register.html", {'error': error})


def password_reset_request(request):
    return render(request, "password_reset.html")


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
