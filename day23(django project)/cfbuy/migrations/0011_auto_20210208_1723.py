# Generated by Django 3.1.5 on 2021-02-08 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cfbuy', '0010_auto_20210208_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cfbuy',
            name='buy_date',
        ),
        migrations.AddField(
            model_name='cfselect',
            name='buy_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='구매일자'),
        ),
    ]
