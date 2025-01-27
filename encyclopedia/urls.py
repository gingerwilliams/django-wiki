from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:wiki>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("new", views.new, name="new"),
    path("edit/<str:wiki>", views.edit, name="edit"),
    path("update", views.update, name="update"),
    path("lucky", views.lucky, name="lucky"),
]