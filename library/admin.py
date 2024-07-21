from django.contrib import admin

from library.models import Book, InstanceBook, DistributionBook, Author, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'publishing_house', 'year', 'pages', 'description')
    list_filter = ('genre', 'year',)
    search_fields = ('title','authors',)


@admin.register(InstanceBook)
class InstanceBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'inventory', 'status')
    list_filter = ('status',)
    search_fields = ('inventory',)


@admin.register(DistributionBook)
class DistributionBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'instance_book', 'issue_date', 'return_date')
    list_filter = ('user', 'return_date')
    search_fields = ('user',)
