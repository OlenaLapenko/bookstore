"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from catalog.views import index, get_books, get_authors, choose_author, choose_book, get_publishers, choose_publisher, \
    get_stores, choose_store, search_books

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('books/', get_books, name='books'),
    path("books/<int:pk>/", choose_book, name="choose_book"),
    path("search", search_books, name="search_books"),
    path('authors/', get_authors, name='authors'),
    path("authors/<int:pk>/", choose_author, name="choose_author"),
    path('publishers/', get_publishers, name='publishers'),
    path("publishers/<int:pk>/", choose_publisher, name="choose_publisher"),
    path('stores/', get_stores, name='stores'),
    path("stores/<int:pk>/", choose_store, name="choose_store"),
    path('__debug__/', include('debug_toolbar.urls')),

]
