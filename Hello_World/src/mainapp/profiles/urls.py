from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profiles_page', views.profiles_page, name="profiles_page"),
    path('<int:pk>/details/', views.details, name="details"),
]
