from django.db import models

import random
import datetime
from faker import Faker

import catalog


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True)

    def __str__(self):
        return f"{self.name}"

    def age(self):
        return datetime.datetime.now().year - self.birthdate.year


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.name}"


class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} id: {self.id}"


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    store = models.ManyToManyField(Store)
    pubdate = models.DateField()

    def __str__(self):
        return f"{self.name} id: {self.id}"

    @staticmethod
    def generate_books_data(books_amount, authors_amount, publishers_amount, stores_amount):
        faker = Faker()

        for _ in range(publishers_amount):
            catalog.models.Publisher.objects.create(
                name=faker.text(max_nb_chars=20),
                city=faker.city()
                )

        for _ in range(authors_amount):
            catalog.models.Author.objects.create(
                name=faker.name(),
                birthdate=faker.date_time_between(start_date="-120y", end_date="-18y"),
                )

        for _ in range(stores_amount):
            catalog.models.Store.objects.create(
                name=faker.text(max_nb_chars=20),
            )

        stores_list = list(Store.objects.all())
        authors_list = list(Author.objects.all())

        for _ in range(books_amount):
            book = Book.objects.create(
                name=faker.text(max_nb_chars=50),
                pages=random.randint(10, 1000),
                price=random.uniform(10, 3000),
                rating=random.randint(0, 10),
                pubdate=faker.date_time_between(start_date="-120y"),
                publisher_id=random.choice(Publisher.objects.values_list('pk', flat=True).order_by('id')),
            )
            book.store.add(random.choice(stores_list))
            book.authors.add(random.choice(authors_list))






