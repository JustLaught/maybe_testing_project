# Generated by Django 4.2.5 on 2023-10-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_bookmark_user_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]