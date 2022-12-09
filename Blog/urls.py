from django.urls import path
from .views import BlogView, BlogDetailsView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('details/<slug:slug>', BlogDetailsView.as_view(), name='blog_details')
]