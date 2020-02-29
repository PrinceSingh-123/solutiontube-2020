from django.contrib import admin
from django.urls import path,include
from myexam import views
from . import views
from rest_framework import routers

from myexam.views import QuestionViewset, ExamViewset, ExamQuestionViewset

router = routers.DefaultRouter()
router.register('question', QuestionViewset)
router.register('exam', ExamViewset)

app_name = 'myexam'

urlpatterns = [
    path('', views.quiz, name='exam'),
    path('api/', include(router.urls)),
]