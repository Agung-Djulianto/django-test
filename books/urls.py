from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_create, name='book_create'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('preview_book/<int:book_id>/', views.book_preview, name='book_preview')
]
