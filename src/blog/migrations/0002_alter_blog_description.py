# Generated by Django 3.2 on 2023-01-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, help_text='descriptions should be maximum of 200 characters and can be blank', max_length=200),
        ),
    ]