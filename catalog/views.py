from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from catalog.models import Book, Author, Publisher, Store


def index(request):
    amount_authors = Author.objects.all().count()
    amount_publishers = Publisher.objects.all().count()
    amount_stores = Store.objects.all().count()
    amount_books = Book.objects.all().count()
    return render(request=request,
                  template_name='index.html',
                  context={
                      'amount_authors': amount_authors,
                      'amount_publishers': amount_publishers,
                      'amount_stores': amount_stores,
                      'amount_books': amount_books,
                  },
                  )


def get_authors(request):
    authors = Author.objects.all().annotate(num_books=Count('book'))
    return render(
        request=request,
        template_name='authors.html',
        context={
            'authors': authors,
        },
    )


def choose_author(request, pk):
    author = get_object_or_404(Author.objects.all().annotate(num_books=Count('book')), pk=pk)
    return render(
        request=request,
        template_name='choose_author.html',
        context={
            'author': author,
        },
    )


def get_publishers(request):
    publishers = Publisher.objects.all().annotate(num_books=Count('book'), avg_price=Avg('book__price'))
    return render(
        request=request,
        template_name='publishers.html',
        context={
            'publishers': publishers,
        },
    )


def choose_publisher(request, pk):
    publisher = get_object_or_404(Publisher.objects.all().annotate(num_books=Count('book')), pk=pk)
    return render(
        request=request,
        template_name='choose_publisher.html',
        context={
            'publisher': publisher,
        },
    )


def get_stores(request):
    stores = Store.objects.all().annotate(num_books=Count('book'), avg_price=Avg('book__price'))
    return render(
        request=request,
        template_name='stores.html',
        context={
            'stores': stores,
        },
    )


def choose_store(request, pk):
    store = get_object_or_404(Store.objects.all().annotate(num_books=Count('book')), pk=pk)
    return render(
        request=request,
        template_name='choose_store.html',
        context={
            'store': store,
        },
    )


def get_books(request):
    books = Book.objects.all().select_related('publisher').prefetch_related('authors')
    avg_price = Book.objects.aggregate(avg=Avg('price'))
    avg_rating = Book.objects.aggregate(avg=Avg('rating'))
    return render(
        request=request,
        template_name='books.html',
        context={
            'books': books,
            'avg_price': avg_price,
            'avg_rating': avg_rating,
        },
    )


def choose_book(request, pk):
    book = get_object_or_404(Book.objects.all(), pk=pk)
    return render(
        request=request,
        template_name='choose_book.html',
        context={
            'book': book,
        },
    )


def search_books(request):
    books = Book.objects.all().select_related('publisher')
    search_text = request.GET.get('search')
    search_fields = ['name', 'publisher__name']
    or_filter = Q()
    for field in search_fields:
        or_filter |= Q(**{f"{field}__icontains": search_text})
    books = books.filter(or_filter)

    return render(request=request, template_name="search_books.html", context={"books": books})








