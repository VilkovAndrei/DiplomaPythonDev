from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import UserViewSet, UserUpdateView, MyTokenObtainPairView, UserRetrieveView, \
    UserCreateView, UserDestroyView

app_name = UsersConfig.name
# router = DefaultRouter()
# router.register(r'profile', UserViewSet, basename='profile')
urlpatterns = ([
    path('profile/create/', UserCreateView.as_view(), name='user_create'),
    path('profile/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('profile/<int:pk>/', UserRetrieveView.as_view(), name='user_detail'),
    path('profile/delete/<int:pk>/', UserDestroyView.as_view(), name='user_delete'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
)
# + router.urls)
