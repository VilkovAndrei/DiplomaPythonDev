from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from library.models import Book, InstanceBook, DistributionBook, Author, Genre
from library.paginators import BooksPagination
from library.serializers import BookSerializer, InstanceBookSerializer, DistributionBookSerializer, AuthorSerializer, GenreSerializer

from users.permissions import UserIsOwner, IsManager


class AuthorCreateAPIView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [IsManager]


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsManager]
    pagination_class = BooksPagination


class GenreCreateAPIView(generics.CreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = [IsManager]


class GenreListView(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsManager]
    pagination_class = BooksPagination


class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsManager]


class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsManager]
    pagination_class = BooksPagination


class BookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsManager]


class BookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsManager]


class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsManager]
