# Generated by Django 4.1.5 on 2023-03-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_userprofile_pronouns'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
