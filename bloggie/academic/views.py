from django.shortcuts import render
from django.http import JsonResponse

from academic.models import Department, Faculty, Level, Course, BorrowedCourse, Orientation


def course_list(request):
    """function to render the list of course according to department"""
    dept: str = request.GET.get("department")  # grab department
    level: str = request.GET.get("level")
    course: Course = Course.objects.filter(department=dept, level=level)
    borrowed: BorrowedCourse = BorrowedCourse.objects.filter(department=dept, level=level)
    faculty: Faculty = Faculty.objects.all()
    level: Level = Level.objects.all()
    context: dict = {"faculty": faculty, 'courses': course, "borrowed": borrowed, "level": level}
    return render(request, "academic/course_list.html", context)


def load_department(request):
    """Ajax call to load department from faculty"""
    faculty_id = request.GET.get('faculty')
    department = Department.objects.filter(faculty=faculty_id).order_by('name')
    return render(request, 'academic/department_dropdown_list_options.html', {'dept': department})


def orientation(request):
    """view to fetch orientation information based on student department"""
    dept: str = request.GET.get("department")  # grab department
    if dept:
        content: Orientation = Orientation.objects.get(department=dept)
    else:
        content = None
    faculty: Faculty = Faculty.objects.all()
    context: dict = {"faculty": faculty, 'orientation': content}
    return render(request, 'academic/orientation.html', context)


def past_question(request):
    context = {"course": "hello"}
    return render(request, 'academic/pass-q.html', context)


def cbt(request):
    return render(request, 'academic/cbt.html')