from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    student_id = models.PositiveIntegerField(unique = True)
    marks = models.PositiveIntegerField()