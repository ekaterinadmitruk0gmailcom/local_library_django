from django.urls import path
from .views import BookListView, BookDetailView, AuthorDetailView, AuthorListView, index,\
    LoanedBooksByUserListView, LoanedBooksAllListView, renew_book_librarian, AuthorCreate, AuthorUpdate, \
    AuthorDelete, BookCreate, BookUpdate, BookDelete


urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('myborrowed/', LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

urlpatterns += [
    path('book/<uuid:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    path('author/create/', AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]

urlpatterns += [
    path('book/create/', BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]