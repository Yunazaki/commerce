# Generated by Django 5.0.1 on 2024-01-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctions_date_listed_auctions_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]