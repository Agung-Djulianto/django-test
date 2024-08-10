from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Book
from .forms import BookForm
from django.db.models import Q
from pdf2image import convert_from_path # type: ignore
import os
from gensim import corpora, models # type: ignore
from gensim.parsing.preprocessing import preprocess_string # type: ignore
from .models import Author, Category, Book
from .models import Author, Category, Book
from .forms import BookForm
from django.contrib import messages


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # Mendapatkan instance Author dan Category dari database
            author_id = request.POST.get('author')
            category_id = request.POST.get('category')
            author = Author.objects.get(id=author_id)
            category = Category.objects.get(id=category_id)

            # Buat instance Book
            book = form.save(commit=False)
            book.author = author
            book.category = category
            book.save()
            return redirect('books:book_list')
        else:
            print(form.errors)
    else:
        form = BookForm()

    authors = Author.objects.all()
    categories = Category.objects.all()
    return render(request, 'add_book.html', {
        'form': form,
        'authors': authors,
        'categories': categories,
    })

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:book_list')


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    authors = Author.objects.all()
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buku berhasil diperbarui!')
            return redirect('books:book_detail', id=book.id)
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan periksa form Anda.')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {
        'form': form,
        'book': book,
        'authors': authors,
        'categories': categories
    })

def book_preview(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_preview.html', {'book': book})