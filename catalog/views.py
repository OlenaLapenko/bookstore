from django.shortcuts import render
from catalog.models import Book, Author


def index(request):
    return render(request=request, template_name='index.html')


def get_books(request):
    books = Book.objects.all()
    return render(
        request=request,
        template_name='books.html',
        context={
            'books': books,
        },
    )


def get_authors(request):
    authors = Author.objects.all()
    return render(
        request=request,
        template_name='authors.html',
        context={
            'authors': authors,
        },
    )