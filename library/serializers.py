from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from library.models import Book, InstanceBook, DistributionBook, Author, Genre
from library.validators import ReturnDateValidator


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('title',)


class DistributionBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = DistributionBook
        extra_kwargs = {'return_date': {'required': True}}
        validators = [ReturnDateValidator(field='return_date')]
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    instance_count = SerializerMethodField()
    authors = AuthorSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=False, read_only=True)

    @staticmethod
    def get_instance_count(instance):
        return InstanceBook.objects.filter(book=instance).count()

    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'genre', 'description', 'publishing_house', 'year', 'pages', 'instance_count')
        read_only_fields = fields


class BookDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=False, read_only=True)
    instance_count = SerializerMethodField()
    instance_books = SerializerMethodField()

    class Meta:
        model = Book
        fields = ('title', 'authors', 'genre', 'description', 'publishing_house', 'year', 'pages', 'instance_count', 'instance_books')
        read_only_fields = fields

    @staticmethod
    def get_instance_count(instance):
        return InstanceBook.objects.filter(book=instance).count()

    @staticmethod
    def get_instance_books(instance):
        return InstanceBookSerializer(InstanceBook.objects.prefetch_related('book').filter(book=instance), many=True).data


class InstanceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstanceBook
        fields = '__all__'

