# python imports

# django imports
from epilepsy12.models import AntiEpilepsyMedicine, MedicineEntity

# E12 imports
from epilepsy12.constants import KPI_SCORE

def score_kpi_8(registration_instance, age_at_first_paediatric_assessment) -> int:
    """8. Sodium Valproate

    Percentage of all females 12 years and above currently on valproate treatment with annual risk acknowledgement form completed

    Calculation Method

    Numerator = Number of females aged 12 and above diagnosed with epilepsy at first year AND on valproate AND annual risk acknowledgement forms completed AND pregnancy prevention programme in place

    Denominator = Number of females aged 12 and above diagnosed with epilepsy at first year AND on valproate
    """
    # ineligible - < 12yo or male
    if age_at_first_paediatric_assessment < 12 or registration_instance.case.sex != 2:
        return KPI_SCORE["INELIGIBLE"]

    # not scored
    if registration_instance.management.has_an_aed_been_given is None:
        return KPI_SCORE["NOT_SCORED"]

    # ineligible
    if not AntiEpilepsyMedicine.objects.filter(
        management=registration_instance.management,
        medicine_entity=MedicineEntity.objects.get(medicine_name="Sodium valproate"),
    ).exists():
        return KPI_SCORE["INELIGIBLE"]

    # get valproate assigned
    valproate = AntiEpilepsyMedicine.objects.get(
        management=registration_instance.management,
        medicine_entity=MedicineEntity.objects.get(medicine_name="Sodium valproate"),
    )

    if (
        valproate.is_a_pregnancy_prevention_programme_needed
        and valproate.has_a_valproate_annual_risk_acknowledgement_form_been_completed
    ):
        return KPI_SCORE["PASS"]
    else:
        return KPI_SCORE["FAIL"]
