from django.contrib import admin
from .models import BillingAddressModel, CountryModel, PaymentDetailModel, CheckoutModel, WishlistModel, CartModel,Cart_item
# Register your models here.

admin.site.register([BillingAddressModel, CountryModel, PaymentDetailModel, CheckoutModel, WishlistModel,CartModel,Cart_item])