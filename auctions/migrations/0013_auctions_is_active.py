# Generated by Django 5.0.1 on 2024-01-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_comments_auction_comments_comment_comments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
