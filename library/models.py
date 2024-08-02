from django.db import models

from config import settings
from users.models import NULLABLE


class StatusBook(models.TextChoices):
    """Статус экземпляра книги"""
    IN_STOCK = "В наличии", "В наличии"
    ISSUED = "Выдана", "Выдана"
    DISCARDED = "Списана", "Списана"
    RESERVED = "Зарезервирована", "Зарезервирована"
    MAINTENANCE = "На обслуживании", "На обслуживании"


class Language(models.Model):
    """Модель языка книги."""
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Язык')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Author(models.Model):
    """Модель автора книги"""
    first_name = models.CharField(max_length=100, default='A', verbose_name='Имя')
    last_name = models.CharField(max_length=100, default='A', verbose_name='Фамилия')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Родился')
    date_of_death = models.DateField('Умер', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


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
    author = models.ForeignKey(Author, related_name="books",on_delete=models.CASCADE, verbose_name='Автор',
                               **NULLABLE)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр', related_name='books')
    publishing_house = models.CharField(max_length=100, verbose_name='Издательство')
    year = models.PositiveIntegerField(verbose_name='Год издания')
    pages = models.PositiveIntegerField(verbose_name='Кол-во страниц')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name='Язык')
    description = models.TextField(max_length=1000, verbose_name='Описание', **NULLABLE)
    isbn = models.CharField(max_length=50, verbose_name='ISBN', **NULLABLE)

    def __str__(self):
        return f'{self.title} ({self.author})'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title', 'author']

    def display_genre(self):
        """Отображает список жанров книги."""
        return ', '.join([genre.title for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'


class InstanceBook(models.Model):
    """Модель экземпляра книги"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга', related_name='instance_books')
    inventory = models.CharField(max_length=24, unique=True, verbose_name='Инвентарный номер')
    status = models.CharField(max_length=50, default=StatusBook.IN_STOCK,
                              choices=StatusBook, verbose_name='Статус экземпляра книги')

    def __str__(self):
        return f'{self.inventory} ({self.book.title}, {self.book.author})'

    class Meta:
        verbose_name = 'Экземпляр книги'
        verbose_name_plural = 'Экземпляры книг'


class DistributionBook(models.Model):
    """Модель выдачи экземпляра книги"""
    instance_book = models.ForeignKey(InstanceBook, on_delete=models.CASCADE, verbose_name='Экземпляр книги',
                                      related_name='distribution_books')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='distribution_books')
    issue_date = models.DateField(auto_now=True, verbose_name="Дата выдачи")
    return_date = models.DateField(verbose_name="Дата возврата")
    is_completed = models.BooleanField(default=False, verbose_name="Признак возврата")

    class Meta:
        verbose_name = 'Выдача книги'
        verbose_name_plural = 'Выдачи книг'
