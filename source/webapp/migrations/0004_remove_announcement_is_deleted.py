# Generated by Django 4.1.6 on 2023-02-11 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_announcement_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='is_deleted',
        ),
    ]
