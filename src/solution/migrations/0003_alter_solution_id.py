# Generated by Django 3.2 on 2023-01-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0002_alter_solution_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
