from django.contrib import admin
from .models import TeamModel, ContactModel, Contact_form

# Register your models here.

admin.site.register([TeamModel, ContactModel,Contact_form])