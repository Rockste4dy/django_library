from django.urls import path
from book import views as w_books

urlpatterns = [
    path('', w_books.index, name='books'),
    path('create/', w_books.create_book, name='create_book'),
    path('<int:book_id>', w_books.get_book, name='read_book'),
    path('update/<int:book_id>/', w_books.update_book, name='update_book'),
    path('delete/<int:book_id>', w_books.delete_book, name='delete_book'),
    path('search/', w_books.search_book),
]