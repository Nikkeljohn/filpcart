# Generated by Django 3.2.20 on 2024-04-25 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
    ]
