from library.models import InstanceBook, Book, DistributionBook


def get_instancebook_list():
    return InstanceBook.objects.select_related('book').order_by("id")


def get_book_list():
    return Book.objects.select_related('author').prefetch_related("genre").all().order_by("id")


def get_distribution_book_list(user):
    return DistributionBook.objects.select_related('user').fiter(is_completed=False, user=user).order_by("id")
