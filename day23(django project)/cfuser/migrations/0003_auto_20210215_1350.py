# Generated by Django 3.1.5 on 2021-02-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfuser', '0002_cfuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfuser',
            name='image',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to='images'),
        ),
    ]
