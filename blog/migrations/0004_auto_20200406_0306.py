# Generated by Django 3.0.5 on 2020-04-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200404_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='media_root/default_featured.jpg', help_text='Upload featured Image', upload_to='bolg', verbose_name='Upload Featured Image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(help_text='Profile Photo', upload_to='profile', verbose_name='Profile Photo'),
        ),
    ]