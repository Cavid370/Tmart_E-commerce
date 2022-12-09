from django.db import models
from User.models import UserModel
from django.utils.text import slugify


# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=500)
    img = models.ImageField(upload_to='blog/')
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogModel, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.created_by}'

class CommentModel(models.Model):
    name = models.CharField(max_length = 30)