from django.forms import ModelForm

from catalog.models import Book, Author


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("name", "pages", "price", "rating", "pubdate")



