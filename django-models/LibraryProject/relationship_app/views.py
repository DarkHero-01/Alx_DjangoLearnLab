from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ Explicitly importing DetailView
from .models import Book, Library  # ✅ Explicitly importing Library

# Function-Based View (FBV) for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View (CBV) for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Create your views here.
