# Generated by Django 5.0.6 on 2024-07-02 19:58

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swapp', '0007_blogpostphoto_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostphoto',
            name='embed_youtube',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
