# Generated by Django 3.1.6 on 2021-02-28 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Age',
            new_name='age',
        ),
    ]
