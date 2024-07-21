from django.db import models

from config import settings
from users.models import NULLABLE


class Author(models.Model):
    """Модель автора книги"""
    name = models.CharField(max_length=100, verbose_name='Имя, фамилия')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    """Модель жанра книги"""
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    """Модель книги"""
    title = models.CharField(max_length=255, verbose_name='Название')
    authors = models.ManyToManyField(Author, related_name="authors", verbose_name='Авторы')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр', related_name='books')
    publishing_house = models.CharField(max_length=100, verbose_name='Издательство')
    year = models.PositiveIntegerField(verbose_name='Год издания')
    pages = models.PositiveIntegerField(verbose_name='Количество страниц')

    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.title} ({self.authors})'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class InstanceBook(models.Model):
    """Модель экземпляра книги"""

    class StatusBook(models.TextChoices):
        """Статус экземпляра книги"""
        IN_STOCK = "В наличии", "В наличии"
        ISSUED = "Выдана", "Выдана"
        DISCARDED = "Списана", "Списана"

    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга', related_name='book')
    inventory = models.CharField(max_length=24, unique=True, verbose_name='Инвентарный номер')
    status = models.CharField(max_length=50, default=StatusBook.IN_STOCK,
                                      choices=StatusBook, verbose_name='Статус экземпляра книги')

    def __str__(self):
        return f'{self.inventory} ({self.book})'

    class Meta:
        verbose_name = 'Экземпляр книги'
        verbose_name_plural = 'Экземпляры книг'


class DistributionBook(models.Model):
    """Модель выдачи экземпляра книги"""
    instance_book = models.ForeignKey(InstanceBook, on_delete=models.CASCADE, verbose_name='Экземпляр книги',
                                      related_name='instance_book')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             null=True)
    issue_date = models.DateTimeField(auto_now=True, verbose_name="Дата выдачи")
    return_date = models.DateTimeField(verbose_name="Дата возврата")
