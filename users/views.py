from rest_framework import viewsets, generics, serializers
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import UserPermissionsDestroy, IsOwner
from users.serializers import (UserSerializer, UserDetailSerializer, UserLimitedSerializer,
                               MyTokenObtainPairSerializer)

from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new_user = serializer.save(is_active=True)
        new_user.set_password(new_user.password)
        new_user.save()


class UserRetrieveView(generics.RetrieveAPIView):
    # serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            self.serializer_class = UserDetailSerializer
        else:
            self.serializer_class = UserLimitedSerializer
        return self.serializer_class


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]


class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [UserPermissionsDestroy]
