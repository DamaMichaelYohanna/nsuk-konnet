from django.contrib import admin

from academic.models import Faculty, Department, Course, Level, BorrowedCourse, Orientation

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Level)
admin.site.register(BorrowedCourse)
admin.site.register(Orientation)