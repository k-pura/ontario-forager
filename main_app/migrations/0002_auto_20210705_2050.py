# Generated by Django 3.2.4 on 2021-07-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='culinary_use',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='medicinal_use',
            field=models.TextField(max_length=1000),
        ),
    ]
