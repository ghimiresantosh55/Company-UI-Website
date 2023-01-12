from django.db import models
from src.core_app.models import CreateInfoModel
# Create your models here.


class Contact(CreateInfoModel):
    name=models.CharField(max_length=50, unique=True, help_text=" name can be max. of 50 characters")
    contact_no = models.CharField(max_length=15, blank=True, help_text="contact no. should be maximum of 15 characters")
    email = models.EmailField(max_length=255, help_text='email address max length: 255 characters', unique=True)
    address = models.TextField(max_length=50, blank=True, help_text="Address should be maximum of 50 characters")
    link=models.CharField(max_length=50, help_text=" name can be max. of 50 characters")
    active = models.BooleanField(default=True, help_text="By default active=True")

    def __str__(self):
        return "id {}".format(self.id)
