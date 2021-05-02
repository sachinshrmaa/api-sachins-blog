
from django.urls import path
from .views import BlogPostListView, BlogPostDetailView


urlpatterns = [
    path('', BlogPostListView.as_view(), name="list-posts"),
    path('<slug>/', BlogPostDetailView.as_view()),
]