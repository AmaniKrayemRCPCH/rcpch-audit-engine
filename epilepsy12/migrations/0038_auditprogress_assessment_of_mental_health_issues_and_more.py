# Generated by Django 4.1.2 on 2022-12-15 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0037_alter_case_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditprogress',
            name='assessment_of_mental_health_issues',
            field=models.IntegerField(default=0, help_text={'label': 'Assessment of mental health issues', 'reference': 'Percentage of children with epilepsy where there is documented evidence that they have been asked about mental health either through clinical screening, or a questionnaire/measure.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='care_planning_has_been_updated_when_necessary',
            field=models.IntegerField(default=0, help_text={'label': 'Care planning has been updated when necessary', 'reference': 'Percentage of children and young people with epilepsy after 12 months where there is evidence that the care plan has been updated where necessary.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='comprehensive_care_planning_agreement',
            field=models.IntegerField(default=0, help_text={'label': 'Comprehensive care planning agreement', 'reference': 'Percentage of children and young people with epilepsy after 12 months where there is evidence of a comprehensive care plan that is agreed between the person, their family and/or carers and primary and secondary care providers, and the care plan has been updated where necessary.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='comprehensive_care_planning_content',
            field=models.IntegerField(default=0, help_text={'label': 'Comprehensive care planning content', 'reference': 'Percentage of children diagnosed with epilepsy with documented evidence of communication regarding core elements of care planning.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='ecg',
            field=models.IntegerField(default=0, help_text={'label': 'ECG', 'reference': 'Percentage of children and young people with convulsive seizures and epilepsy, with an ECG at first year.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='epilepsy_specialist_nurse',
            field=models.IntegerField(default=0, help_text={'label': 'Epilepsy Specialist Nurse', 'reference': 'Percentage of children and young people with epilepsy, with input by epilepsy specialist nurse within the first year of care.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='epilepsy_surgery_referral',
            field=models.IntegerField(default=0, help_text={'label': 'Epilepsy surgery referral', 'reference': 'Percentage of ongoing children and young people meeting defined epilepsy surgery referral criteria with evidence of epilepsy surgery referral.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='first_aid',
            field=models.IntegerField(default=0, help_text={'label': 'First aid', 'reference': ''}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='general_participation_and_risk',
            field=models.IntegerField(default=0, help_text={'label': 'General participation and risk', 'reference': ''}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='mental_health_support',
            field=models.IntegerField(default=0, help_text={'label': 'Mental health support', 'reference': 'Percentage of children with epilepsy and a mental health problem who have evidence of mental health support'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='mri',
            field=models.IntegerField(default=0, help_text={'label': 'MRI', 'reference': 'Percentage of children and young people with defined indications for an MRI, who had who had timely MRI within 6 weeks of request'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='paediatrician_with_expertise_in_epilepsies',
            field=models.IntegerField(default=0, help_text={'label': 'Paediatrician with expertise in epilepsies', 'reference': 'Percentage of children and young people with epilepsy, with input by a ‘consultant paediatrician with expertise in epilepsies’ within 2 weeks of initial referral'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='parental_prolonged_seizures_care_plan',
            field=models.IntegerField(default=0, help_text={'label': 'Parental prolonged seizures care plan', 'reference': ''}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='patient_carer_parent_agreement_to_the_care_planning',
            field=models.IntegerField(default=0, help_text={'label': 'Patient/carer/parent agreement to the care planning', 'reference': 'Percentage of children and young people with epilepsy after 12 months where there was evidence of agreement between the person, their family and/or carers as appropriate.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='patient_held_individualised_epilepsy_document',
            field=models.IntegerField(default=0, help_text={'label': 'Patient-held individualised epilepsy document/copy of clinic letter that includes care planning information', 'reference': 'Percentage of children and young people with epilepsy after 12 months that had an individualised epilepsy document with individualised epilepsy document or a copy clinic letter that includes care planning information.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='school_individual_healthcare_plan',
            field=models.IntegerField(default=0, help_text={'label': 'School individualised health care plan', 'reference': ''}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='service_contact_details',
            field=models.IntegerField(default=0, help_text={'label': 'Service contact details', 'reference': ''}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='sodium_valproate',
            field=models.IntegerField(default=0, help_text={'label': 'Sodium Valproate', 'reference': 'Percentage of all females 12 years and above currently on valproate treatment with annual risk acknowledgement form completed'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='sudep',
            field=models.IntegerField(default=0, help_text={'label': 'Sudden unexplained death in epilepsy', 'reference': ''}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='tertiary_input',
            field=models.IntegerField(default=0, help_text={'label': 'Tertiary input', 'reference': 'Percentage of children and young people meeting defined criteria for paediatric neurology referral, with input of tertiary care and/or CESS referral within the first year of care.'}, null=True),
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='water_safety',
            field=models.IntegerField(default=0, help_text={'label': 'Water safety', 'reference': ''}, null=True),
        ),
    ]
