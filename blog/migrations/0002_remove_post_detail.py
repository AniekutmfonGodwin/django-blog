# Generated by Django 3.0.5 on 2020-04-04 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='detail',
        ),
    ]