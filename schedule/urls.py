from django.urls import path
from . import views

urlpatterns = [
    path(
        route='', 
        view=views.dashboard, 
        name='dashboard'
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