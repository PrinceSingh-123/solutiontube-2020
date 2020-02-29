from django.shortcuts import render
from django.http import HttpResponse
from myexam.models import Question,Exam
from myexam.serializers import QuestionSerialzer, ExamSerializer
from rest_framework import viewsets


# view for the quiz.
def quiz(request):
    return render(request,'exam.html')

  # viewsets for rest_framework

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialzer


class ExamViewset(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamQuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerialzer
    queryset = Question.objects.filter(exam_id = 1)
    def get_queryset(self):
        return Question.objects.filter(exam_id=self.kwargs.get('pk'))


