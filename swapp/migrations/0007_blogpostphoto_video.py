# Generated by Django 5.0.6 on 2024-07-02 17:33

import swapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swapp', '0006_alter_blogpost_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostphoto',
            name='video',
            field=models.FileField(blank=True, upload_to='', validators=[swapp.models.validate_file_extension]),
        ),
    ]
