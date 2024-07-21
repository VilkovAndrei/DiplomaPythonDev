from rest_framework.serializers import ValidationError
from datetime import datetime, timedelta


class ReturnDateValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        now_time = datetime.now()
        return_date = value.get('return_date')
        if return_date <= now_time:
            raise ValidationError('Дата возврата книги не может быть ранее завтрашнего дня.')
        else:
            return None
