from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("load", views.load, name="load"),
]