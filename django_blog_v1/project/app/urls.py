from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('contact',views.contact),
    path('about',views.about),
]