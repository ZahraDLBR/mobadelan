# Generated by Django 2.1 on 2018-08-26 04:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180825_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_msg',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
