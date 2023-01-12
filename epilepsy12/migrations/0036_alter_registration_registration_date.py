# Generated by Django 4.1.2 on 2022-12-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0035_registration_audit_submission_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='registration_date',
            field=models.DateField(default=None, help_text={'label': 'First paediatric assessment', 'reference': 'Setting this date is an irreversible step. Confirmation will be requested to complete this step.'}, null=True),
        ),
    ]
