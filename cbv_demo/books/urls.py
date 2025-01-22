from django.urls import path
from .views import (
    HomePageView, BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
