# Generated by Django 4.1.5 on 2023-05-31 09:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social_sharing', '0009_alter_comment_pin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownpin',
            name='description',
        ),
        migrations.RemoveField(
            model_name='ownpin',
            name='destination_link',
        ),
        migrations.RemoveField(
            model_name='ownpin',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ownpin',
            name='title',
        ),
        migrations.AddField(
            model_name='pin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
