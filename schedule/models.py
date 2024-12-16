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
    ROOM_CHOICES = [
    ('G01', 'G01'), ('G02', 'G02'), ('G03', 'G03'), ('G04', 'G04'), ('G05', 'G05'),
    ('G06', 'G06'), ('G07', 'G07'), ('G08', 'G08'), ('G09', 'G09'), ('G10', 'G10'),
    ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'),
    ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109'), ('110', '110'),
    ('201', '201'), ('202', '202'), ('203', '203'), ('204', '204'), ('205', '205'),
    ('206', '206'), ('207', '207'), ('208', '208'), ('209', '209'), ('210', '210'),
    ('301', '301'), ('302', '302'), ('303', '303'), ('304', '304'), ('305', '305'),
    ('306', '306'), ('307', '307'), ('308', '308'), ('309', '309'), ('310', '310'),
    ]
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    #on_delete means that when delete major with id in schedule, delete the schedule as well
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=1) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
    teacher_name = models.CharField(max_length=255)
    room = models.CharField(max_length=10, choices=ROOM_CHOICES)
    time_begins = models.CharField(max_length=5)
    time_ends = models.CharField(max_length=5)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)

