# Generated by Django 3.0.5 on 2020-04-06 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200406_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(auto_now=True, verbose_name='Date Publish'),
        ),
    ]
