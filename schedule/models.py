from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=255)

class Subject(models.Model):
    name = models.CharField(max_length=255)

class Schedule(models.Model):
    major_id = models.IntegerField()
    subject_id = models.IntegerField()
    teacher_name = models.CharField(max_length=255)
    room = models.CharField(max_length=50)
    time_begins = models.CharField(max_length=5)
    time_ends = models.CharField(max_length=5)
    day = models.CharField(max_length=20)

