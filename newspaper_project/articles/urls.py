from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
)

urlpatterns = [
    path(',<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),              # new edit
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),           # new detail
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),           # new delete
    path('', ArticleListView.as_view(), name='article_list'),                               # new article
]