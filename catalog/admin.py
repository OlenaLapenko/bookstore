from django.contrib import admin

from catalog.models import Author, Book, Publisher, Store


class BookInline(admin.TabularInline):
    model = Book
    extra = 2


class BookAuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 2


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('pubdate', 'rating')
    fields = ['name', 'pages', 'price', 'rating', 'authors',
              'publisher', 'pubdate']
    list_display = ('name', 'pages', 'price', 'rating',
                    'publisher', 'pubdate')
    search_fields = (
        'name',
    )
    date_hierarchy = 'pubdate'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookAuthorInline, ]
    list_display = ['name']
    search_fields = (
        'name',
    )


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [BookInline, ]
    search_fields = (
        'name',
    )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = (
        'name',
    )



