from django.contrib import admin

from catalog.models import Author, Book, Publisher, Store


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'rating',
                    'pubdate')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']



