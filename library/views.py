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


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]


class AuthorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]


class AuthorDestroyAPIView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsManager]


class AuthorListAPIView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsManager]
    pagination_class = BooksPagination


class GenreCreateAPIView(generics.CreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = [IsManager]


class GenreListAPIView(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsManager]
    pagination_class = BooksPagination


class GenreRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticated]


class GenreUpdateAPIView(generics.UpdateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticated]


class GenreDestroyAPIView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    permission_classes = [IsManager]


class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsManager]


class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    # queryset = Book.objects.all().order_by('id')
    queryset = Book.objects.all().prefetch_related('authors').order_by('id')
    permission_classes = [IsAuthenticated]
    pagination_class = BooksPagination


class BookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


class BookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]


class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsManager]


class InstancebookCreateAPIView(generics.CreateAPIView):
    serializer_class = InstanceBookSerializer
    permission_classes = [IsManager]


class InstancebookListAPIView(generics.ListAPIView):
    serializer_class = InstanceBookSerializer
    # queryset = Book.objects.all().order_by('id')
    queryset = InstanceBook.objects.all().select_related('book').order_by('id')
    permission_classes = [IsAuthenticated]
    pagination_class = BooksPagination


class InstancebookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = InstanceBookSerializer
    queryset = InstanceBook.objects.all()
    permission_classes = [IsAuthenticated]


class InstancebookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = InstanceBookSerializer
    queryset = InstanceBook.objects.all()
    permission_classes = [IsAuthenticated]


class InstancebookDestroyAPIView(generics.DestroyAPIView):
    queryset = InstanceBook.objects.all()
    permission_classes = [IsManager]
