from User.models import SubscriberEmail
from .serializers import MyTokenObtainPairSerializer, SubscriberEmailSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework import generics
User= get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class SubscriberEmailView(generics.ListCreateAPIView):
    serializer_class = SubscriberEmailSerializer
    queryset = SubscriberEmail.objects.all()