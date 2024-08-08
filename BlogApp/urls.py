from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllPostView.as_view()),
    path("<int:pk>", views.SinglePost.as_view()),
    path("category/<int:pk>", views.SingleCategoryView.as_view()),
    path("category", views.AllCategoryView.as_view()),
    path("tag/<int:pk>", views.SingleTagView.as_view()),
    path("tag", views.AllTagView.as_view()),
    path("popular", views.PopularView.as_view()),
    path("author", views.AllAuthorView.as_view()),
    path("author/<int:pk>", views.SingleAuthorView.as_view()),
    path("recent", views.RecentView.as_view()),
    path("social", views.SocialView.as_view()),
    path("liver", views.WithoutPagination.as_view()),
]
