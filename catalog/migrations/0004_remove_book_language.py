# Generated by Django 3.0.1 on 2019-12-29 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191229_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
    ]
