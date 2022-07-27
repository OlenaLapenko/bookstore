from django.db import models

import random
import datetime
from faker import Faker


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True)

    def age(self):
        return datetime.datetime.now().year - self.birthdate.year

    def generate_authors(self, count):
        faker = Faker()
        for _ in range(count):
            Author.objects.create(
                name=faker.name(),
                birthdate=faker.date_time_between(start_date="-120y", end_date="-18y"),
                )


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def generate_publishers(self, count):
        faker = Faker()
        for _ in range(count):
            Author.objects.create(
                name=faker.text(max_nb_chars=20),
                )


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
#    publisher = models.ForeignKey('catalog.Publisher', on_delete=models.CASCADE)
    pubdate = models.DateField()

    def generate_books(self, count):
        faker = Faker()
        for _ in range(count):
            Author.objects.create(
                name=faker.text(max_nb_chars=50),
                pages=random.randint(10, 1000),
                price=random.uniform(10, 3000),
                rating=random.uniform(0, 10),
                pubdate=faker.date_time_between(start_date="-120y")
                )


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def generate_publishers(self, count):
        faker = Faker()
        for _ in range(count):
            Author.objects.create(
                name=faker.text(max_nb_chars=20),
                )


class Store(models.Model):
    name = models.CharField(max_length=100)

    def generate_stores(self, count):
        faker = Faker()
        for _ in range(count):
            Author.objects.create(
                name=faker.text(max_nb_chars=20),
                )