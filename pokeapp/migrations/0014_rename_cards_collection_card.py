# Generated by Django 4.2.7 on 2023-12-05 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0013_rename_trainers_collection_trainer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='cards',
            new_name='card',
        ),
    ]