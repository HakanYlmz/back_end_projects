from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('',views.admin),
    path('/get_people',views.get_people),
    path('sendBlog',views.sendBlog)
]
