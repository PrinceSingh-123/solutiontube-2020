from django.urls import path

from mytutorial import views

app_name = 'mytutorial'

urlpatterns = [

    path('', views.tutorial, name='tutorial'),

]  