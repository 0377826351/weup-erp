# Generated by Django 4.0.4 on 2022-08-04 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_delete_members'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]