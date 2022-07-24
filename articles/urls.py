from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDraftListView,
    ArticleDraftDetailView,
    redirect_view,
)

urlpatterns = [
    path('articles/1/1/', redirect_view),
    path('<section>/<status>/', ArticleListView.as_view(), name='article_list'),
    path('<section>', ArticleListView.as_view(), name='article_list'),
    path('drafts/', ArticleDraftListView.as_view(), name='article_draft_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/draft/', ArticleDraftDetailView.as_view(), name='article_draft_detail'),
    path('<int:pk>/<section>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/<section>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
]