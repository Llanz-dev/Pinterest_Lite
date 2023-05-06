# Generated by Django 3.2.16 on 2023-04-11 05:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_sharing', '0008_comment_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='hearts',
        ),
        migrations.AddField(
            model_name='comment',
            name='hearts',
            field=models.ManyToManyField(related_name='comment_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]