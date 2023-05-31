from django.db import models
from froala_editor.fields import FroalaField


class Faculty(models.Model):
    """model for faculties"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class Department(models.Model):
    """model for faculties"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    faculty = models.ForeignKey(Faculty, related_name='faculty', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Level(models.Model):
    """model for the different levels of the student"""
    level = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.level}"


class Course(models.Model):
    """model for different course with respect to their department """
    code = models.CharField(max_length=7, null=True)
    title = models.CharField(max_length=50)
    pre = models.ForeignKey("Course", on_delete=models.DO_NOTHING, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title}"


class BorrowedCourse(models.Model):
    """Table for borrowed courses."""
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.course}'


class Orientation(models.Model):
    """model for departmental orientation and information """
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    content = FroalaField()
    date = models.DateField(auto_created=True)

    def __str__(self):
        return f"{self.department}"

