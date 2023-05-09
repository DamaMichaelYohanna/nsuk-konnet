from django.db import models


class Faculty(models.Model):
    """model for faculties"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class Department(models.Model):
    """model for faculties"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    faculty = models.ForeignKey(Faculty, related_name='faculty', on_delete=models.CASCADE)


class Level(models.Model):
    """model for the different levels of the student"""
    level = models.CharField(max_length=3)


class Course(models.Model):
    """model for different course with respect to their department """
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)