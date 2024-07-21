from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import UserUpdateView, MyTokenObtainPairView, UserRetrieveView, \
    UserCreateView, UserDestroyView, UserListView

app_name = UsersConfig.name
# router = DefaultRouter()
# router.register(r'profile', UserViewSet, basename='profile')
urlpatterns = ([
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/list/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/', UserRetrieveView.as_view(), name='user_detail'),
    path('users/delete/<int:pk>/', UserDestroyView.as_view(), name='user_delete'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
)
# + router.urls)
