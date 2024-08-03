from celery import shared_task

import smtplib
from datetime import datetime
from django.core.mail import send_mail
import pytz
from django.conf import settings
from loguru import logger
from library.models import DistributionBook


logger.add("logs/mailing.log", format="{time} {level} {message}", level="INFO", rotation="1 month")


@shared_task
def send_mailing():
    logger.info("Задача напоминания о сроке возврата книг запущена.")
    subject = "Напоминание о сроке возврата книги в библиотеку: "
    message = ("Здравствуйте! Срок возврата книг(и) в библиотеку прошел. Если Вы хотите изменить срок возврата,"
               " пожалуйста, свяжитесь с нами.")

    zone = pytz.timezone(settings.TIME_ZONE)
    current_date = datetime.now(zone).date()
    distr_books = DistributionBook.objects.select_related("instance_book").filter(return_date__lt=current_date,
                                                                                  is_completed=False).order_by('user')
    logger.info(f"Количество выданных книг с прошедшим сроком возврата - {len(distr_books)}")
    previous_user = None
    for distr_book in distr_books:
        current_user = distr_book.user
        current_inctance_book = str(distr_book.instance_book)

        if current_user != previous_user:
            try:
                send_mail(
                        subject=subject+current_inctance_book,
                        message=message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[current_user.email],
                        fail_silently=False
                )
                server_response = (f"Сообщение пользователю {current_user.email} о сроке возврата книги"
                                   f" {current_inctance_book} отправлено успешно.")
                logger.info(server_response)

            except smtplib.SMTPResponseException as response:
                server_response = f"Сообщение пользователю {current_user.email} о сроке возврата книги" + str(response)
                logger.info(server_response)

        previous_user = current_user

    return
