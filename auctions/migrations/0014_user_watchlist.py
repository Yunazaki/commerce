# Generated by Django 5.0.1 on 2024-01-12 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auctions_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(related_name='watchlist', to='auctions.auctions'),
        ),
    ]
