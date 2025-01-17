from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'category', 'isbn', 'publisher', 'publication_date', 'num_pages', 'language', 'pdf', 'cover']
