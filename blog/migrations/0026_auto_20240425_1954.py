# Generated by Django 3.2.20 on 2024-04-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20240425_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
