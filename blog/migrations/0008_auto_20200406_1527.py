# Generated by Django 3.0.5 on 2020-04-06 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200406_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='profile',
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ManyToManyField(to='blog.Profile'),
        ),
    ]
