from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("songs", views.song, name="songs"),
    path("record", views.record, name="record"),
]
