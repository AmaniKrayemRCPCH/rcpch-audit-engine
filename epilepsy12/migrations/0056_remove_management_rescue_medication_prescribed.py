# Generated by Django 4.0.4 on 2022-08-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0055_rename_investigation_complete_auditprogress_investigations_complete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='management',
            name='rescue_medication_prescribed',
        ),
    ]