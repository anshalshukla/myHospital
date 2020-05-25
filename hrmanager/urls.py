from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('',view),
    path('update_doctor_form/<int:id>/', update_doctor_form),
    path('update_doctor/<int:id>/', update_doctor),
    path('delete_doctor/<int:id>/', delete_doctor),
]