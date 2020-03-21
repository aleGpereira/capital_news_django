from django.urls import path

from . import views
from .views import (PostCreateView, PostDeleteView, PostDetailView,
                    PostListView, PostUpdateView, UserPostListView)

urlpatterns = [
    path('', PostListView.as_view(), name='news-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='reporter-posts'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='news-detail'),
    path('news/new/', PostCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/update/', PostUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', PostDeleteView.as_view(), name='news-delete'),
    path('about/', views.about, name='news-about')
]
