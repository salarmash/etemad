from django.urls import path
from . import views

urlpatterns = [
    path("", views.ServiceView.as_view(), name="Index"),
    path("<int:pk>", views.SingService.as_view()),
    path("faq", views.FAQView.as_view()),
    path("vision", views.VisionView.as_view()),
    path("about", views.AboutView.as_view()),
    path("contact", views.ContactView.as_view()),
    path("sidebar", views.SidebarView.as_view()),
    path("feature", views.FeatureView.as_view()),
    path("counter", views.Counter.as_view()),
]
