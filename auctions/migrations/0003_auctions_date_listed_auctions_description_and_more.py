# Generated by Django 5.0.1 on 2024-01-08 17:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctions_bids_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='date_listed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='auctions',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='auctions',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='auctions',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]