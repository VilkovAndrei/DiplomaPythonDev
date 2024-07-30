from django.contrib import admin

from library.models import Book, InstanceBook, DistributionBook, Author, Genre, Language, StatusBook

admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    list_filter = ('last_name',)
    search_fields = ('last_name',)
    inlines = [BookInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title',)


class InstanceBookInline(admin.TabularInline):
    model = InstanceBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publishing_house', 'year', 'pages', 'description', 'language', 'isbn')
    list_filter = ('genre', 'year', 'language')
    search_fields = ('title', 'author',)
    inlines = [InstanceBookInline]


@admin.register(InstanceBook)
class InstanceBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'inventory', 'status')
    list_filter = ('status',)
    search_fields = ('inventory',)


@admin.register(DistributionBook)
class DistributionBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'instance_book', 'issue_date', 'return_date', 'is_completed')
    list_filter = ('user', 'return_date', 'is_completed')
    search_fields = ('user',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "instance_book":
            kwargs["queryset"] = InstanceBook.objects.filter(status=StatusBook.IN_STOCK)
        return super(DistributionBookAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
