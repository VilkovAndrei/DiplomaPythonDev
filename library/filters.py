import django_filters
from library.models import Book, Genre


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__last_name', lookup_expr='icontains', label='Фамилия автора')
    genre = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all(), field_name='genre',
                                                     lookup_expr='icontains', label='Жанр')

    class Meta:
        model = Book
        fields = ['genre', 'title', 'author']
