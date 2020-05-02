from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, PostCategoryListView
from . import views
from blog import views as blog_views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path("<slug>/", PostDetailView.as_view(), name="blog-detail"),
    path("post/new/", PostCreateView.as_view(), name="blog-create"),
    path("<slug>/update/", PostUpdateView.as_view(), name="blog-update"),
    path("<slug>/delete/", PostDeleteView.as_view(), name="blog-delete"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path("category/<slug>/", PostCategoryListView.as_view(), name="blog-category"),
]
