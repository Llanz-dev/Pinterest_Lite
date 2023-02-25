# Generated by Django 4.1.5 on 2023-02-22 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(error_messages={'invalid': "Sorry, this doesn't look like a valid email"}, max_length=254, null=True, validators=[django.core.validators.EmailValidator()])),
                ('age', models.PositiveSmallIntegerField()),
                ('password', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
