from datetime import timezone

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.fields import SerializerMethodField

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserDetailSerializer(serializers.ModelSerializer):
    distr_books = SerializerMethodField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'distr_books')

    @staticmethod
    def get_distr_books(instance):
        pass
        # return PaymentSerializer(Payment.objects.filter(user=instance), many=True).data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['email'] = user.email

        return token

    # def post(self, request, *args, **kwargs):
    #     email = request.data.get("email")
    #     if User.objects.filter(email=email).exists():
    #         user = User.objects.get(email=email)
    #         user.last_login = timezone.now()
    #         user.save()
    #
    #     return super().post(request)