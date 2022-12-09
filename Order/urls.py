from django.urls import path
from .views import CartView, WishlistView ,CheckoutView


urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('wishlist/', WishlistView.as_view(), name='wishlist')
]