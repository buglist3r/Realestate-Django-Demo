# Generated by Django 2.1.7 on 2019-04-08 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lisiting',
            new_name='Listing',
        ),
    ]