from django.urls import path

from . import views

app_name = 'mysolution'

urlpatterns = [

    path('', views.solution, name='solution'),

]    