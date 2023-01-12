# Generated by Django 3.2 on 2023-01-11 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import src.blog.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_ad', models.DateTimeField()),
                ('created_date_bs', models.CharField(max_length=10)),
                ('device_type', models.PositiveBigIntegerField(choices=[(1, 'Mobile'), (2, 'PC'), (3, 'Tablet'), (4, 'Other'), (5, 'NA')], default=5, help_text='where 1=Mobile, 2=PC, 3=Tablet and 4=Other')),
                ('app_type', models.PositiveBigIntegerField(choices=[(1, 'Web-App'), (2, 'IOS-App'), (3, 'Android-App'), (4, 'NA')], default=4, help_text='where 1=Web-App, 2=IOS-APP, 3=Android-APP')),
                ('name', models.CharField(help_text=' name can be max. of 50 characters', max_length=50, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='blog', validators=[src.blog.models.validate_image])),
                ('description', models.TextField(blank=True, help_text='Address should be maximum of 50 characters', max_length=200)),
                ('active', models.BooleanField(default=True, help_text='By default active=True')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]