# Generated by Django 3.2.4 on 2021-06-10 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0003_auto_20210610_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer',
            old_name='acc_no_of_sender',
            new_name='Acc_No',
        ),
        migrations.AlterField(
            model_name='transfer',
            name='Date_Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
