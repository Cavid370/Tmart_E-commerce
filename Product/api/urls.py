import django
from django.urls import path
from .views import *
urlpatterns =[
    path('product/', ProductView.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),
]