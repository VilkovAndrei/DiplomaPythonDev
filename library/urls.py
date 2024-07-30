from django.urls import path

from library.apps import LibraryConfig

from library.views import (BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, \
      BookDestroyAPIView, InstancebookCreateAPIView, InstancebookListAPIView, InstancebookRetrieveAPIView, \
      InstancebookUpdateAPIView, InstancebookDestroyAPIView, DistributionBookCreateAPIView, \
      DistributionBookListAPIView, \
      DistributionBookRetrieveAPIView, DistributionBookUpdateAPIView, DistributionBookDestroyAPIView, AuthorViewSet, \
      GenreViewSet)

      # AuthorCreateAPIView, AuthorListAPIView, AuthorRetrieveAPIView, AuthorUpdateAPIView, \
      # AuthorDestroyAPIView, GenreCreateAPIView, GenreListAPIView, GenreRetrieveAPIView, GenreUpdateAPIView, \
      # GenreDestroyAPIView,

from rest_framework.routers import DefaultRouter


app_name = LibraryConfig.name
router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'genres', GenreViewSet, basename='genres')

urlpatterns = [
      path('books/create/', BookCreateAPIView.as_view(), name='book_create'),
      path('books/', BookListAPIView.as_view(), name='book_list'),
      path('books/<int:pk>/view/', BookRetrieveAPIView.as_view(), name='book_view'),
      path('books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),
      path('books/<int:pk>/delete/', BookDestroyAPIView.as_view(), name='book_delete'),
      # path('authors/create/', AuthorCreateAPIView.as_view(), name='author_create'),
      # path('authors/', AuthorListAPIView.as_view(), name='author_list'),
      # path('authors/<int:pk>/view/', AuthorRetrieveAPIView.as_view(), name='author_view'),
      # path('authors/<int:pk>/update/', AuthorUpdateAPIView.as_view(), name='author_update'),
      # path('authors/<int:pk>/delete/', AuthorDestroyAPIView.as_view(), name='author_delete'),
      # path('genres/create/', GenreCreateAPIView.as_view(), name='genre_create'),
      # path('genres/', GenreListAPIView.as_view(), name='genre_list'),
      # path('genres/<int:pk>/view/', GenreRetrieveAPIView.as_view(), name='genre_view'),
      # path('genres/<int:pk>/update/', GenreUpdateAPIView.as_view(), name='genre_update'),
      # path('genres/<int:pk>/delete/', GenreDestroyAPIView.as_view(), name='genre_delete'),
      path('instance_books/create/', InstancebookCreateAPIView.as_view(), name='instancebook_create'),
      path('instance_books/', InstancebookListAPIView.as_view(), name='instancebook_list'),
      path('instance_books/<int:pk>/view/', InstancebookRetrieveAPIView.as_view(), name='instancebook_view'),
      path('instance_books/<int:pk>/update/', InstancebookUpdateAPIView.as_view(), name='instancebook_update'),
      path('instance_books/<int:pk>/delete/', InstancebookDestroyAPIView.as_view(), name='instancebook_delete'),
      path('distribution_books/create/', DistributionBookCreateAPIView.as_view(), name='distributionbook_create'),
      path('distribution_books/', DistributionBookListAPIView.as_view(), name='distributionbook_list'),
      path('distribution_books/<int:pk>/view/', DistributionBookRetrieveAPIView.as_view(),
           name='distributionbook_view'),
      path('distribution_books/<int:pk>/update/', DistributionBookUpdateAPIView.as_view(),
           name='distributionbook_update'),
      path('distribution_books/<int:pk>/delete/', DistributionBookDestroyAPIView.as_view(),
           name='distributionbook_delete')
]

urlpatterns += router.urls
