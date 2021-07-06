# Generated by Django 3.2.4 on 2021-07-06 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('culinary_use', models.TextField(max_length=250)),
                ('medicinal_use', models.TextField(max_length=250)),
                ('harvest_season', models.CharField(max_length=250)),
                ('cautions', models.TextField(max_length=250)),
            ],
        ),
    ]
