from django.shortcuts import render


def course_list(request):
    return render(request, "academic/course_list.html")
