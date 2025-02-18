# Generated by Django 4.2 on 2023-04-24 13:51

# Python
from operator import itemgetter

# Third-party Imports
from django.db import migrations

# RCPCH Imports
from ..constants import SYNDROMES
from ..models import SyndromeList


def seed_syndromes(apps, schema_editor):
    """
    This function seeds the Syndrome model with a list of syndromes.
    It should be run periodically to check if the data has already been seeded and to avoid duplicates.

    Parameters:
        apps (list): A list of installed apps
        schema_editor (object): A database schema editor object

    Returns:
        None
    """
    added = 0
    print("\033[33m", "Seeding all the syndromes...", "\033[33m")
    for syndrome in sorted(SYNDROMES, key=itemgetter(1)):
        if SyndromeList.objects.filter(syndrome_name=syndrome[1]).exists():
            print("Syndromes already exist. Skipping this step...")
            return
        new_syndrome = SyndromeList(
            syndrome_name=syndrome[1],
        )
        try:
            new_syndrome.save()
        except Exception as e:
            print(f"Error at {syndrome[1]}: error: {e}")
        added += 1
        print(f"added {syndrome[1]}")
    print(f"Syndromes added...{added}")


class Migration(migrations.Migration):
    dependencies = [
        ("epilepsy12", "0007_seed_semiology_keywords"),
    ]

    operations = [migrations.RunPython(seed_syndromes)]
