# Generated by Django 4.0.4 on 2022-09-08 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0003_alter_epilepsy12user_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case',
            options={'permissions': (('can_view_child_nhs_number', "Can view a child's NHS Number"), ('can_view_child_date_of_birth', "Can view a child's date of birth"), ('can_delete_child_case_data', "Can irreversibly delete a child's case data."), ('can_update_child_case_data', "Can edit or update a child's case data."), ('can_lock_child_case_data_from_editing', "Can lock a child's record from editing."), ('can_unlock_child_case_data_from_editing', "Can unlock a child's record from editing."), ('can_opt_out_child_from_inclusion_in_audit', "Can sanction an opt out from participating in the audit. Note all the child's date except Epilepsy12 unique identifier are irretrievably deleted."), ('can_view_child_case_data', "Can view a child's demographic and case information.")), 'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.AlterModelOptions(
            name='epilepsy12user',
            options={'permissions': [('can_consent_to_audit_participation', 'Can consent to participating in Epilepsy12.')], 'verbose_name': 'Epilepsy12 User', 'verbose_name_plural': 'Epilepsy12 Users'},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'permissions': [('can_approve_eligibility', 'Can approve eligibility for Epilepsy12.'), ('can_remove_approval_of_eligibility', 'Can remove approval of eligibiltiy for Epilepsy12.'), ('can_view_lead_clinician', 'Can view the lead clinician'), ('can_allocate_lead_clinician', 'Can allocate the lead clinician.'), ('can_edit_lead_clinician', 'Can edit the lead clinician.'), ('can_register_child_in_epilepsy12', 'Can register child in Epilepsy12. (A cohort number is automatically allocaeted)'), ('can_unregister_child_in_epilepsy12', 'Can unregister a child in Epilepsy. Their record and previously entered data is untouched.')], 'verbose_name': 'Registration', 'verbose_name_plural': 'Registrations'},
        ),
    ]
