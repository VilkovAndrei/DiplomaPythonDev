# Generated by Django 5.0.6 on 2024-07-29 18:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_language_alter_book_options_remove_author_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='books', to='library.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='distributionbook',
            name='instance_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distribution_books', to='library.instancebook', verbose_name='Экземпляр книги'),
        ),
        migrations.AlterField(
            model_name='distributionbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distribution_books', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='instancebook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instance_books', to='library.book', verbose_name='Книга'),
        ),
    ]
