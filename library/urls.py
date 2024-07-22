from django.urls import path

from library.apps import LibraryConfig

from library.views import BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, \
    BookDestroyAPIView, AuthorCreateAPIView, AuthorListAPIView, AuthorRetrieveAPIView, AuthorUpdateAPIView, \
    AuthorDestroyAPIView, GenreCreateAPIView, GenreListAPIView, GenreRetrieveAPIView, GenreUpdateAPIView, \
    GenreDestroyAPIView, InstancebookCreateAPIView, InstancebookListAPIView, InstancebookRetrieveAPIView, \
    InstancebookUpdateAPIView, InstancebookDestroyAPIView, DistributionBookCreateAPIView, DistributionBookListAPIView, \
    DistributionBookRetrieveAPIView, DistributionBookUpdateAPIView, DistributionBookDestroyAPIView

app_name = LibraryConfig.name

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
      path('instbook/create/', InstancebookCreateAPIView.as_view(), name='instancebook_create'),
      path('instbook/list/', InstancebookListAPIView.as_view(), name='instancebook_list'),
      path('instbook/view/<int:pk>/', InstancebookRetrieveAPIView.as_view(), name='instancebook_view'),
      path('instbook/update/<int:pk>/', InstancebookUpdateAPIView.as_view(), name='instancebook_update'),
      path('instbook/delete/<int:pk>/', InstancebookDestroyAPIView.as_view(), name='instancebook_delete'),
      path('distrbook/create/', DistributionBookCreateAPIView.as_view(), name='distributionbook_create'),
      path('distrbook/list/', DistributionBookListAPIView.as_view(), name='distributionbook_list'),
      path('distrbook/view/<int:pk>/', DistributionBookRetrieveAPIView.as_view(), name='distributionbook_view'),
      path('distrbook/update/<int:pk>/', DistributionBookUpdateAPIView.as_view(), name='distributionbook_update'),
      path('distrbook/delete/<int:pk>/', DistributionBookDestroyAPIView.as_view(), name='distributionbook_delete'),
]
