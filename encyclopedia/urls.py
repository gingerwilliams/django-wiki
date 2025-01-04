from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:wiki>", views.wiki, name="wiki"),
    path("wiki/", views.search, name="search")
]