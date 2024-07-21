from django.urls import path

from library.apps import LibraryConfig
from rest_framework.routers import DefaultRouter

from library.views import BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, \
    BookDestroyAPIView

app_name = LibraryConfig.name
# router = DefaultRouter()
# router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('book/create/', BookCreateAPIView.as_view(), name='book_create'),
                  path('book/list/', BookListAPIView.as_view(), name='book_list'),
                  path('book/view/<int:pk>/', BookRetrieveAPIView.as_view(), name='book_view'),
                  path('book/update/<int:pk>/', BookUpdateAPIView.as_view(), name='book_update'),
                  path('book/delete/<int:pk>/', BookDestroyAPIView.as_view(), name='book_delete')
              ]

