from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookSearchForm

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic to handle creation
    return render(request, 'bookshelf/create_book.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to handle editing
    return render(request, 'bookshelf/edit_book.html', {'book': book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to handle deletion
    return render(request, 'bookshelf/delete_book.html', {'book': book})

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = []
    if form.is_valid():
        query = form.cleaned_data.get('title')
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})

# Create your views here.
