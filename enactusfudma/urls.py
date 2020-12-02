from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('alumni', views.alumni, name='alumni'),
     path('project', views.project, name='project'),
     path('activestudent', views.activeStudent, name='activestudent'),
     path('sdg1', views.sdg1, name='sdg1'),
     path('sdg2', views.sdg2, name='sdg2'),
     path('sdg3', views.sdg3, name='sdg3'),
     path('sdg4', views.sdg4, name='sdg4'),
     path('sdg5', views.sdg5, name='sdg5'),
     path('sdg6', views.sdg6, name='sdg6'),
     path('sdg7', views.sdg7, name='sdg7'),
     path('sdg8', views.sdg8, name='sdg8'),
     path('sdg9', views.sdg9, name='sdg9'),
     path('sdg10', views.sdg10, name='sdg10'),
     path('sdg11', views.sdg11, name='sdg11'),
     path('sdg12', views.sdg12, name='sdg12'),
     path('sdg13', views.sdg13, name='sdg13'),
     path('sdg14', views.sdg14, name='sdg14'),
     path('sdg15', views.sdg15, name='sdg15'),
     path('sdg16', views.sdg16, name='sdg16'),
     path('sdg17', views.sdg17, name='sdg17'),





]