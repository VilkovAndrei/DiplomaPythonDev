# Generated by Django 5.0.6 on 2024-07-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_book_isbn_alter_book_author_alter_book_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ISBN'),
        ),
    ]