# Generated by Django 5.0.6 on 2024-06-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swapp', '0003_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
