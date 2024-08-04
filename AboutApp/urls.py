from django.urls import path
from . import views

app_name = "About"

urlpatterns = [
    path("", views.AboutView.as_view(), name="Index"),
    path("process", views.ProcessView.as_view()),
    path('partner', views.PartnerView.as_view()),
]
