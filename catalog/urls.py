from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('my books/', views.LoanedBookListView.as_view(), name='my_borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew_book_librarian'),

]
