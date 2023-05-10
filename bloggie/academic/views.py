from django.shortcuts import render
from django.http import JsonResponse

from academic.models import Department, Faculty

from academic.models import Course


def course_list(request):
    if request.method == "GET":

        dept = request.GET.get("department")
        level = request.GET.get("level")
        if dept and level:
            course = Course.objects.filter(department=dept, level=level)
        else:
            course = None
    faculty = Faculty.objects.all()
    context = {"faculty": faculty, 'courses': course}
    return render(request, "academic/course_list.html", context)


def load_department(request):
    faculty_id = request.GET.get('faculty')
    department = Department.objects.filter(faculty=faculty_id).order_by('name')
    return render(request, 'academic/department_dropdown_list_options.html', {'dept': department})
