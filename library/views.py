from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from library.models import Book, InstanceBook, DistributionBook, Author, Genre, StatusBook
from library.paginators import BooksPagination, GenresPagination, AuthorsPagination, DistributionBooksPagination
from library.serializers import (BookSerializer, InstanceBookSerializer, DistributionBookSerializer, AuthorSerializer,
                                 GenreSerializer)
from library.services_db import get_instancebook_list, get_book_list

from users.permissions import IsManager


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all().order_by('id')
    pagination_class = AuthorsPagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsManager]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated | IsManager]
        elif self.action in ['retrieve', 'update']:
            self.permission_classes = [IsManager]
        elif self.action == 'destroy':
            self.permission_classes = [IsManager]
        return [permission() for permission in self.permission_classes]


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all().order_by('id')
    pagination_class = GenresPagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsManager]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated | IsManager]
        elif self.action in ['retrieve', 'update']:
            self.permission_classes = [IsManager]
        elif self.action == 'destroy':
            self.permission_classes = [IsManager]
        return [permission() for permission in self.permission_classes]


class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsManager]


class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BooksPagination

    def get_queryset(self):
        return get_book_list()


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


class InstancebookCreateAPIView(generics.CreateAPIView):
    serializer_class = InstanceBookSerializer
    permission_classes = [IsManager]


class InstancebookListAPIView(generics.ListAPIView):
    serializer_class = InstanceBookSerializer
    queryset = get_instancebook_list()
    permission_classes = [IsManager]
    pagination_class = BooksPagination


class InstancebookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = InstanceBookSerializer
    queryset = InstanceBook.objects.select_related("book").all()
    permission_classes = [IsManager]


class InstancebookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = InstanceBookSerializer
    queryset = InstanceBook.objects.all()
    permission_classes = [IsManager]


class InstancebookDestroyAPIView(generics.DestroyAPIView):
    queryset = InstanceBook.objects.all()
    permission_classes = [IsManager]


class DistributionBookCreateAPIView(generics.CreateAPIView):
    serializer_class = DistributionBookSerializer
    permission_classes = [IsManager]

    def perform_create(self, serializer):
        if serializer.is_valid():
            new_distr = serializer.save()
            instance_book = InstanceBook.objects.filter(id=new_distr.instance_book_id).first()
            # print(instance_book.status)
            instance_book.status = StatusBook.ISSUED
            instance_book.save()
            new_distr.save()


class DistributionBookListAPIView(generics.ListAPIView):
    serializer_class = DistributionBookSerializer
    permission_classes = [IsManager | IsAuthenticated]
    pagination_class = DistributionBooksPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = DistributionBook.objects.select_related('instance_book').all().order_by("id")
        elif user.groups.filter(name='manager').exists():
            queryset = DistributionBook.objects.select_related('instance_book').filter(is_completed=False).order_by("id")
        else:
            queryset = DistributionBook.objects.select_related('instance_book').filter(user=user, is_completed=False).order_by("id")
        return queryset


class DistributionBookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = DistributionBookSerializer
    queryset = DistributionBook.objects.all()
    permission_classes = [IsManager]

    # def perform_update(self, serializer):
    #     if serializer.is_valid():
    #         update_distr = serializer.save()
    #         if update_distr.is_completed:
    #             update_distr.instance_book.status = StatusBook.IN_STOCK
    #         update_distr.save()


class DistributionBookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DistributionBookSerializer
    queryset = DistributionBook.objects.all()
    permission_classes = [IsManager]


class DistributionBookDestroyAPIView(generics.DestroyAPIView):
    queryset = DistributionBook.objects.all()
    permission_classes = [IsManager]
