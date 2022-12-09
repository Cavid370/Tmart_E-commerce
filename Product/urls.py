from django.urls import path
from .views import customer_review,TagPageView, ProductDetailView

urlpatterns = [
    path('', TagPageView.as_view(), name = 'product'),
    # path('detail/<slug:slug>/', product_detail, name = 'product_detail'),
    path('review/', customer_review, name = 'customer_review'),
    path('product_detail/<slug:slug>', ProductDetailView.as_view(), name="product_detail"),
    # path('product_detail', product_detail, name = 'product_detail'),
]