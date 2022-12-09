from email.policy import default
from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from datetime import datetime

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    img = models.ImageField(upload_to='category/',default = 'empty',null = True, blank =True)
    is_navbar=models.BooleanField(default=True)
    have_child=models.BooleanField(default=True)
    parent_category_name=models.ForeignKey("Category", on_delete=models.CASCADE, null= True, blank=True, related_name = "Category")
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural= "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True, unique= True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class ProductModel(models.Model):
    name = models.CharField(max_length = 300)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)],null=True,blank=True)
    description = models.TextField()
    new_price = models.IntegerField(null=False, blank=False,default=0)
    old_price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now = True)
    in_sale = models.BooleanField(default=False)
    img = models.ImageField(upload_to='product/')
    img_s = models.ImageField(upload_to='product/img_s/',null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique= True)
    tags = models.ManyToManyField(Tag, blank = True)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs = {"slug": self.slug})
    def soft_delete(self):
        self.is_delete = True
        self.deleted_at = datetime.now()
        self.save()
    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductModel, self).save(*args, **kwargs)

class ProductVersionModel(models.Model):
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self) -> str:
        return f'{self.product_id}'


class ProductColorModel(models.Model):
    color = models.CharField(max_length = 20)
    product_version_id = models.ForeignKey(ProductVersionModel, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='color/')
    def __str__(self) :
        return self.color

class ProductSizeModel(models.Model):
    size = models.CharField(max_length = 5)
    product_version_id = models.ForeignKey(ProductVersionModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.size

class FeaturesModel(models.Model):
    feature = models.TextField()
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.feature

class DataSheetModel(models.Model):
    data = models.TextField()
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self) :
        return self.data

class ReviewsModel(models.Model):
    name = models.CharField(max_length = 30)
    review = models.TextField()
    email = models.EmailField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='reviews/',default = 'empty',null = True, blank =True)
    rate = models.FloatField()
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class ProductStatistic(models.Model):
    product_id = models.ForeignKey(ProductModel, on_delete= models.CASCADE)
    read_count = models.PositiveIntegerField(default=0)
    review_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.product_id} - statistic'