from django.db import models
from django.utils import timezone
# from src.core_app.models import CreateInfoModel
from soori_website import settings
# imports for log
# from simple_history import register
from src.custom_lib.functions.date_converter import ad_to_bs_converter


class CustomGroup(models.Model):
    name = models.CharField(max_length=50, help_text="Name can have max of 50 characters")
    is_active = models.BooleanField(default=True, help_text="by default=True")
    permissions = models.ManyToManyField('CustomPermission', blank=True, help_text="blank=True")
    created_date_ad = models.DateTimeField(default=timezone.now)
    created_date_bs = models.CharField(max_length=10)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk} : {self.name}"

    def save(self, *args, **kwargs):
        # saving created_date_ad and bs, when it is a create operation
        if not self.id:
            self.created_date_ad = timezone.now()
            date_bs = ad_to_bs_converter(self.created_date_ad)
            self.created_date_bs = date_bs

        super().save(*args, **kwargs)





class PermissionCategory(models.Model):
    name = models.CharField(max_length=50, help_text="Name can have max of 50 characters")
    created_date_ad = models.DateTimeField(default=timezone.now)
    created_date_bs = models.CharField(max_length=10)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"ID-{self.id} : {self.name}"

    def save(self, *args, **kwargs):
        # saving created_date_ad and bs, when it is a create operation
        if not self.id:
            self.created_date_ad = timezone.now()
            date_bs = ad_to_bs_converter(self.created_date_ad)
            self.created_date_bs = date_bs

        super().save(*args, **kwargs)




class CustomPermission(models.Model):
    name = models.CharField(max_length=50, help_text="Name can have max of 50 characters")
    code_name = models.CharField(max_length=50, help_text="Code Name can have max of 50 characters")
    category = models.ForeignKey('PermissionCategory', on_delete=models.PROTECT, null=True, blank=True,
                                 help_text="null=Ture, blank=True")
    created_date_ad = models.DateTimeField(default=timezone.now)
    created_date_bs = models.CharField(max_length=10)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.category} : {self.code_name} "

    def save(self, *args, **kwargs):

        self.code_name = str(self.code_name).lower()
        # saving created_date_ad and bs, when it is a create operation
        if not self.id:
            self.created_date_ad = timezone.now()
            date_bs = ad_to_bs_converter(self.created_date_ad)
            self.created_date_bs = date_bs
        super().save(*args, **kwargs)






