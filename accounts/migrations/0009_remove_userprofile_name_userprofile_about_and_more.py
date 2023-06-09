# Generated by Django 4.1.5 on 2023-03-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile_is_active_userprofile_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pronouns',
            field=models.CharField(choices=[('ey/em', 'ey/em'), ('ne/nem', 'ne/nem'), ('she/her', 'she/her'), ('they/them', 'they/them'), ('ve/ver', 've/ver'), ('xe/xem', 'xe/xem'), ('xie/xem', 'xie/xem'), ('ze/zer', 'ze/zer')], default='ey/em', max_length=20),
        ),
    ]
