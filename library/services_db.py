from library.models import InstanceBook, Book


def get_instancebook_list():
    return InstanceBook.objects.select_related('book').order_by("id")


def get_book_list():
    return Book.objects.select_related('author').prefetch_related("genre").all().order_by("id")
