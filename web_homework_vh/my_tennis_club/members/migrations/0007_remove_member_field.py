# Generated by Django 5.0 on 2023-12-10 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_field_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='field',
        ),
    ]