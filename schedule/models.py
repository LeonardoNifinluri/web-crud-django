from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Schedule(models.Model):
    #on_delete means that when delete major with id in schedule, delete the schedule as well
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=1) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
    teacher_name = models.CharField(max_length=255)
    room = models.CharField(max_length=50)
    time_begins = models.CharField(max_length=5)
    time_ends = models.CharField(max_length=5)
    day = models.CharField(max_length=20)

