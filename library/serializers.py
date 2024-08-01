from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from library.models import Book, InstanceBook, DistributionBook, Author, Genre, StatusBook
from library.validators import ReturnDateValidator
from loguru import logger


logger.add("logs/distributions_book.log", format="{time} {level} {message}", level="INFO", rotation="1 week")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'last_name', 'first_name')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookShortSerializer(serializers.ModelSerializer):
    author = AuthorShortSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author')
        read_only_fields = fields


class BookSerializer(serializers.ModelSerializer):
    instance_count = SerializerMethodField()
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    @staticmethod
    def get_instance_count(instance):
        return InstanceBook.objects.filter(book=instance).count()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre', 'description', 'publishing_house', 'year', 'pages',
                  'instance_count')
        read_only_fields = fields


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    instance_books = SerializerMethodField()

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'publishing_house', 'year', 'pages', 'isbn',
                  'instance_books')
        read_only_fields = fields

    @staticmethod
    def get_instance_books(instance):
        return InstanceBookSerializer(InstanceBook.objects.select_related('book').filter(book=instance),
                                      many=True).data


class InstanceBookSerializer(serializers.ModelSerializer):
    book = BookShortSerializer(read_only=True)

    class Meta:
        model = InstanceBook
        fields = ('id', 'book', 'inventory', 'status')


class DistributionBookSerializer(serializers.ModelSerializer):
    # instance_book = InstanceBookSerializer(read_only=True)

    class Meta:
        model = DistributionBook
        extra_kwargs = {'return_date': {'required': True}}
        # validators = [ReturnDateValidator(field='return_date')]
        fields = ('id', 'user', 'instance_book', 'issue_date', 'return_date', 'is_completed')

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.save()
        instance_book_id = instance.instance_book.id
        logger.info(f'Статус экземпляра книги id:{instance_book_id} будет обновлён на ВЫДАНА')
        inst_obj = None
        if instance_book_id:
            inst_obj = InstanceBook.objects.get(id=instance_book_id)
            inst_obj.status = StatusBook.ISSUED
            inst_obj.save()
            logger.info(f'Статус экземпляра книги {inst_obj} обновлён на ВЫДАНА')

        logger.info(f'Выдача экземпляра книги {inst_obj} оформлена.')
        return instance

    def update(self, instance, validated_data):
        instance_book_id = instance.instance_book.id
        logger.info(f'Статус экземпляра книги id:{instance_book_id} будет обновлён на В НАЛИЧИИ')
        instance.instance_book = validated_data.get('instance_book', instance.instance_book)
        instance.user = validated_data.get('user', instance.user)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)
        instance.return_date = validated_data.get('return_date', instance.return_date)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        # is_completed = validated_data.get("is_completed")
        if instance.is_completed:
            logger.info(f'Статус выдачи экземпляра книги id:{instance_book_id} - Книга возвращена.')
            if instance_book_id:
                inst_obj = get_object_or_404(InstanceBook.objects.filter(id=instance_book_id))
                inst_obj.status = StatusBook.IN_STOCK
                inst_obj.save()
                logger.info(f'Статус экземпляра книги {inst_obj} обновлён на В НАЛИЧИИ')
                logger.info(f'Возврат экземпляра книги {inst_obj} оформлен.')
        instance = super().update(instance, validated_data)
        instance.save()
        return instance
