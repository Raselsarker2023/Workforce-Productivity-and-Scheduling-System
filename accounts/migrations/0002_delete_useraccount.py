# Generated by Django 5.0 on 2024-03-19 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]