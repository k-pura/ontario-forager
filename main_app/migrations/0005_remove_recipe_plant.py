# Generated by Django 3.2.4 on 2021-08-12 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_recipe_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='plant',
        ),
    ]