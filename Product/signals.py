from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import ProductModel, ProductStatistic,ProductVersionModel
from django.utils.text import slugify


@receiver(post_save, sender=ProductModel)
def post_save_func(sender, instance, *args, **kwargs):
    # if create:
        ProductStatistic.objects.create (
            product_id = instance
        )

@receiver(post_save, sender=ProductModel)
def post_save_func(sender, instance, *args, **kwargs):
    # if create:
        ProductVersionModel.objects.create (
            product_id = instance
        )

@receiver(pre_save, sender=ProductModel)
def pre_save_func(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)