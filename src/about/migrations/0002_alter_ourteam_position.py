# Generated by Django 3.2 on 2023-01-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='position',
            field=models.CharField(help_text=' name can be max. of 50 characters', max_length=50),
        ),
    ]