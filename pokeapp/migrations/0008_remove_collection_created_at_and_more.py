# Generated by Django 4.2.7 on 2023-12-05 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0007_remove_collection_pokemon_cards_collection_card_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='pokemoncard',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pokemoncard',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='updated_at',
        ),
    ]