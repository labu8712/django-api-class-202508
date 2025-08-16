from django.urls import path

from server.apps.playground.views import HiView, hello

urlpatterns = [
    path("hello", hello),
    path("hi", HiView.as_view()),
]
