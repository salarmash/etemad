from django.urls import path
from . import views

urlpatterns = [
    path("home/hero", views.HeroView.as_view()),
    path("home/about", views.AboutView.as_view()),
    path("home/idea", views.IdeaView.as_view()),
    path("home/service", views.ServiceView.as_view()),
    path("home/advantage", views.AdvantageView.as_view()),
    path("home/work", views.HowWeWorkView.as_view()),
    path("home/core", views.CoreView.as_view()),
]
