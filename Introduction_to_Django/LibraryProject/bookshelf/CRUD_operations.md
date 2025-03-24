# CRUD Operations for the Book Model

This document contains the Create, Retrieve, Update, and Delete (CRUD) operations performed on the `Book` model in Django.

---

## **1. Create a Book**
### **Command:**
```python
from bookshelf.models import Book

# Creating a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Display the created book
print(book)
