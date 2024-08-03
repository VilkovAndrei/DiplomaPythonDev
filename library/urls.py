from django.urls import path

from library.apps import LibraryConfig

from library.views import (BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView,
                           BookDestroyAPIView, InstancebookCreateAPIView, InstancebookListAPIView,
                           InstancebookRetrieveAPIView,
                           InstancebookUpdateAPIView, InstancebookDestroyAPIView, DistributionBookCreateAPIView,
                           DistributionBookListAPIView,
                           DistributionBookRetrieveAPIView, DistributionBookUpdateAPIView,
                           DistributionBookDestroyAPIView, AuthorViewSet, GenreViewSet
                           )

from rest_framework.routers import DefaultRouter


app_name = LibraryConfig.name
router = DefaultRouter()
router.register(r'api/authors', AuthorViewSet, basename='author')
router.register(r'api/genres', GenreViewSet, basename='genre')

urlpatterns = [
      path('api/books/create/', BookCreateAPIView.as_view(), name='book_create'),
      path('api/books/', BookListAPIView.as_view(), name='book_list'),
      path('api/books/<int:pk>/view/', BookRetrieveAPIView.as_view(), name='book_view'),
      path('api/books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),
      path('api/books/<int:pk>/delete/', BookDestroyAPIView.as_view(), name='book_delete'),
      path('api/instance_books/create/', InstancebookCreateAPIView.as_view(), name='instancebook_create'),
      path('api/instance_books/', InstancebookListAPIView.as_view(), name='instancebook_list'),
      path('api/instance_books/<int:pk>/view/', InstancebookRetrieveAPIView.as_view(), name='instancebook_view'),
      path('api/instance_books/<int:pk>/update/', InstancebookUpdateAPIView.as_view(), name='instancebook_update'),
      path('api/instance_books/<int:pk>/delete/', InstancebookDestroyAPIView.as_view(), name='instancebook_delete'),
      path('api/distribution_books/create/', DistributionBookCreateAPIView.as_view(), name='distributionbook_create'),
      path('api/distribution_books/', DistributionBookListAPIView.as_view(), name='distributionbook_list'),
      path('api/distribution_books/<int:pk>/view/', DistributionBookRetrieveAPIView.as_view(),
           name='distributionbook_view'),
      path('api/distribution_books/<int:pk>/update/', DistributionBookUpdateAPIView.as_view(),
           name='distributionbook_update'),
      path('api/distribution_books/<int:pk>/delete/', DistributionBookDestroyAPIView.as_view(),
           name='distributionbook_delete')
]

urlpatterns += router.urls
