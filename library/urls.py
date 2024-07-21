from django.urls import path

from library.apps import LibraryConfig
from rest_framework.routers import DefaultRouter

from library.views import BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, \
    BookDestroyAPIView, AuthorCreateAPIView, AuthorListAPIView, AuthorRetrieveAPIView, AuthorUpdateAPIView, \
    AuthorDestroyAPIView, GenreCreateAPIView, GenreListAPIView, GenreRetrieveAPIView, GenreUpdateAPIView, \
    GenreDestroyAPIView, InstancebookCreateAPIView, InstancebookListAPIView, InstancebookRetrieveAPIView, \
    InstancebookUpdateAPIView, InstancebookDestroyAPIView

app_name = LibraryConfig.name
# router = DefaultRouter()
# router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
      path('book/create/', BookCreateAPIView.as_view(), name='book_create'),
      path('book/list/', BookListAPIView.as_view(), name='book_list'),
      path('book/view/<int:pk>/', BookRetrieveAPIView.as_view(), name='book_view'),
      path('book/update/<int:pk>/', BookUpdateAPIView.as_view(), name='book_update'),
      path('book/delete/<int:pk>/', BookDestroyAPIView.as_view(), name='book_delete'),
      path('author/create/', AuthorCreateAPIView.as_view(), name='author_create'),
      path('author/list/', AuthorListAPIView.as_view(), name='author_list'),
      path('author/view/<int:pk>/', AuthorRetrieveAPIView.as_view(), name='author_view'),
      path('author/update/<int:pk>/', AuthorUpdateAPIView.as_view(), name='author_update'),
      path('author/delete/<int:pk>/', AuthorDestroyAPIView.as_view(), name='author_delete'),
      path('genre/create/', GenreCreateAPIView.as_view(), name='genre_create'),
      path('genre/list/', GenreListAPIView.as_view(), name='genre_list'),
      path('genre/view/<int:pk>/', GenreRetrieveAPIView.as_view(), name='genre_view'),
      path('genre/update/<int:pk>/', GenreUpdateAPIView.as_view(), name='genre_update'),
      path('genre/delete/<int:pk>/', GenreDestroyAPIView.as_view(), name='genre_delete'),
      path('instancebook/create/', InstancebookCreateAPIView.as_view(), name='instancebook_create'),
      path('instancebook/list/', InstancebookListAPIView.as_view(), name='instancebook_list'),
      path('instancebook/view/<int:pk>/', InstancebookRetrieveAPIView.as_view(), name='instancebook_view'),
      path('instancebook/update/<int:pk>/', InstancebookUpdateAPIView.as_view(), name='instancebook_update'),
      path('instancebook/delete/<int:pk>/', InstancebookDestroyAPIView.as_view(), name='instancebook_delete'),
]

