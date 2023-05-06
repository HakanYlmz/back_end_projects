from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('',views.admin),
    path('sendBlog',views.sendBlog)
]
