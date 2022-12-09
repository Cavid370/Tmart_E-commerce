
from email.policy import default
from django.db import models
from User.models import UserModel
from Product.models import ProductVersionModel
# Create your models here.


class BillingAddressModel(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone = models.CharField(max_length = 14)
    message = models.TextField()
    company = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zip_code = models.CharField(max_length = 30)
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.first_name}'

class CountryModel(models.Model):
    name = models.CharField(max_length = 40)
    def __str__(self):
        return f'{self.name}'

class PaymentDetailModel(models.Model):
    card_name = models.CharField(max_length = 20)
    card_number = models.CharField(max_length = 20)
    card_date = models.DateTimeField()
    secure_code = models.CharField(max_length = 256)
    def __str__(self):
        return f'{self.card_number}'


class CheckoutModel(models.Model):
    billing_id = models.ForeignKey(BillingAddressModel, on_delete = models.CASCADE)
    payment_id = models.ForeignKey(PaymentDetailModel, on_delete = models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)

    def __str__(self):
        return self.user_id

class WishlistModel(models.Model):
    is_active = models.BooleanField(default=1)
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    product_version_id = models.ForeignKey(ProductVersionModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.user_id.username}'

class Cart_item(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(ProductVersionModel, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True )
    total = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user_id.username}'s card item {self.product.product_id.name}"

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

class CartModel(models.Model):
    is_active = models.BooleanField(default=1)
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    cart_items = models.ForeignKey(Cart_item, on_delete = models.DO_NOTHING)
    def __str__(self):
        return f"{self.user_id}'s card {self.cart_items.product.product_id.name}"

