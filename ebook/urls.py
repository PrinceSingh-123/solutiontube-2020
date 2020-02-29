from django.urls import path
from ebook import views

app_name = 'ebook'

urlpatterns = [

    path('', views.book_search, name='book'),
    
]  