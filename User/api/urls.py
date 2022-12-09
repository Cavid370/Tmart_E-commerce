from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyObtainTokenPairView,RegisterView, SubscriberEmailView

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('subscribe/', SubscriberEmailView.as_view(), name = 'subscribe')
]

