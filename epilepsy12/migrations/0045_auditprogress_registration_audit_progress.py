# Generated by Django 4.0.4 on 2022-08-20 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0044_remove_registration_assessment_complete_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_complete', models.BooleanField(default=False, null=True)),
                ('initial_assessment_complete', models.BooleanField(default=False, null=True)),
                ('assessment_complete', models.BooleanField(default=False, null=True)),
                ('epilepsy_context_complete', models.BooleanField(default=False, null=True)),
                ('multiaxial_description_complete', models.BooleanField(default=False, null=True)),
                ('investigation_management_complete', models.BooleanField(default=False, null=True)),
            ],
            options={
                'verbose_name': 'Audit Progress',
            },
        ),
        migrations.AddField(
            model_name='registration',
            name='audit_progress',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='epilepsy12.auditprogress'),
        ),
    ]