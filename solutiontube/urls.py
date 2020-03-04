
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

# from apps
from payment import views
from mytutorial.views import tutorial_autocomplete
from mysolution.views import solution_autocomplete
from ebook.views import ebook_autocomplete

urlpatterns = [

    path('',views.index, name='home'),
    path('about/', views.contact, name='contact'),
    path('home/', views.home, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

     # Ebook url forwarding 

    path('ebook/', include('ebook.urls')),
    # Ebook URL forwarding
    url(r'^api/ebook-autocomplete/', ebook_autocomplete, name='ebook-autocomplete'), 
    # Tutorial URL forwarding 

    path('mytutorial/', include('mytutorial.urls')),

    # Turorial auto-complete URL forwarding  
    url(r'^api/company-autocomplete/', tutorial_autocomplete, name='company-autocomplete'),
     
    # Mysolution URL forwarding
    path('mysolution/', include('mysolution.urls')),
    # Mysolution URL forwarding
    url(r'^api/solution-autocomplete/', solution_autocomplete, name='solution-autocomplete'), 
    # Exam URL forwarding

    path('quiz/', include('myexam.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# for static files

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from solutiontube import settings

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  