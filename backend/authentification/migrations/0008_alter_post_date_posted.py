# Generated by Django 4.2.7 on 2023-11-16 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0007_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
