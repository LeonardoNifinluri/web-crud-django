from django.urls import path
from . import views

urlpatterns = [
    path(
        route='', 
        view=views.dashboard, 
        name='dashboard'
    ),
    path(
        route='getSchedules/',
        view=views.get_schedules,
        name='getSchedules'
    ),
    path(
        route='getMajors/',
        view=views.get_majors,
        name='getMajors'
    ),
    path(
        route='getSubjects/',
        view=views.get_subjects,
        name='getSubjects'
    ),
    path(
        route='createSchedule/',
        view=views.create_schedule,
        name='createSchedule'
    ),
    path(
        route='createMajor/',
        view=views.create_major,
        name='createMajor'
    ),
    path(
        route='createSubject/',
        view=views.create_subject,
        name='createSubject'
    ),
    path(
        route='delete/<int:id>/',
        view=views.destroy,
        name='delete'
    ),
    path(
        route='update/<int:id>/',
        view=views.update,
        name='update'
    ),
]