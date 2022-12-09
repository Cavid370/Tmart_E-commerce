from django.urls import path
from .views import IndexPageView, about, contact, team

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('team/', team, name = 'team')
]