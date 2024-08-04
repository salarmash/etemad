from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllProjectView.as_view()),
    path("<int:pk>", views.ProjectView.as_view()),
    path("category", views.CategoryView.as_view()),
    path("benefit", views.BenefitView.as_view()),
]
