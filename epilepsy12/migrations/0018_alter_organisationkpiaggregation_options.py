# Generated by Django 4.2.7 on 2023-11-18 13:51

from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):
    dependencies = [
        ("epilepsy12", "0017_alter_registration_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="organisationkpiaggregation",
            options={
                "ordering": [django.db.models.functions.text.Upper("abstraction_name")],
                "permissions": [
                    (
                        "can_publish_epilepsy12_data",
                        "Can publish epilepsy12 data to public facing site.",
                    )
                ],
                "verbose_name": "Organisation KPI Aggregation Model",
                "verbose_name_plural": "Organisation KPI Aggregation Models",
            },
        ),
    ]