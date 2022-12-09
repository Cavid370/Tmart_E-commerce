from django.db import models

# Create your models here.

class TeamModel(models.Model):
    team_member_name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='team')
    facebook_url = models.CharField(max_length = 500)
    twitter_url = models.CharField(max_length = 500)
    instagram_url = models.CharField(max_length = 500)
    gmail_url = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return self.team_member_name

class ContactModel(models.Model):
    location = models.CharField(max_length = 400)
    phone = models.CharField(max_length = 14)
    mail = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return self.mail

class Contact_form(models.Model):
    full_name = models.CharField(max_length=30)
    mail = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self) -> str:
        return self.full_name