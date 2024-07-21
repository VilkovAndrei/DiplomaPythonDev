from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from library.models import Book, InstanceBook, DistributionBook, Author, Genre
from library.validators import ReturnDateValidator


class DistributionBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = DistributionBook
        extra_kwargs = {'return_date': {'required': True}}
        validators = [ReturnDateValidator(field='return_date')]
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    instance_count = SerializerMethodField()

    @staticmethod
    def get_instance_count(instance):
        return InstanceBook.objects.filter(book=instance).count()

    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'description', 'publishing_house', 'year', 'pages', 'instance_count')


class BookDetailSerializer(serializers.ModelSerializer):
    instance_count = SerializerMethodField()
    instance_books = SerializerMethodField()

    class Meta:
        model = Book
        fields = ('title', 'authors', 'description', 'publishing_house', 'year', 'pages', 'instance_count', 'instance_books')

    @staticmethod
    def get_instance_count(instance):
        return InstanceBook.objects.filter(book=instance).count()

    @staticmethod
    def get_instance_books(instance):
        return InstanceBookSerializer(InstanceBook.objects.filter(book=instance), many=True).data


class InstanceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstanceBook
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
