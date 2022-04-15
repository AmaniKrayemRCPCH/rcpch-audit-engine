# Generated by Django 4.0 on 2022-04-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0007_remove_hospitaltrust_epilepsy12__hospita_a838eb_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Address1',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Address2',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Address3',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='City',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='County',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Email',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Fax',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Latitude',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Longitude',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='OrganisationName',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='ParentName',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='ParentODSCode',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Phone',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Postcode',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltrust',
            name='Website',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
