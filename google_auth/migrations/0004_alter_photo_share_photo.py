# Generated by Django 4.1.2 on 2022-11-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_auth', '0003_alter_photo_share_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo_share',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
