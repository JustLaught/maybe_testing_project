# Generated by Django 4.2.5 on 2023-10-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_comment_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['publication_date', 'author', 'tags']},
        ),
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Views'),
        ),
    ]
