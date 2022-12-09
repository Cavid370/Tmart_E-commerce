from django.urls import path
from .views import ProductVersionAPI, WishlistAPI,BasketAPI

urlpatterns = [
    path('wishlist/', WishlistAPI.as_view(), name = "wishlists"),
    path('product_versions/', ProductVersionAPI.as_view(), name = "product_versions"),
    path('basket/', BasketAPI.as_view(), name="basket"),
    ]