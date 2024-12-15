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
        route='create/',
        view=views.create,
        name='create'
    ),
    path(
        route='update/<int:id>/',
        view=views.update,
        name='update'
    ),
]