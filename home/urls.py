from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns =[

    # path('', home, name='home'),
    # path('home2/', home2, name='home2'),
    # path('update_student/<id>', update_student, name='update_student'),
    # path('delete_student/<id>', delete_student, name='update_student'),

  path('student/',studentAPI.as_view()),


]
