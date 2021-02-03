from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('api/', CreateAppointment.as_view(), name='create-appointemtns-api')
]
