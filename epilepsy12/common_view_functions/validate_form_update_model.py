# python imports
from datetime import datetime
from dateutil.relativedelta import relativedelta

# django imports
from django.utils import timezone
from django.apps import apps

# third party imports
from psycopg2 import DatabaseError

# RCPCH imports
from ..general_functions import current_cohort_start_date, first_tuesday_in_january
from ..validators import epilepsy12_date_validator


def validate_and_update_model(
    request,
    model_id,
    model,
    field_name,
    page_element,
    comparison_date_field_name=None,
    is_earliest_date=None,
    earliest_allowable_date=None,
):
    """
    This is called from the view to update the model or return an error
    Parameters:
    request
    model_id
    model: the class, not the instance
    field_name
    page_element: string one of 'date_field', 'toggle_button', 'multiple_choice_single_toggle_button', 'multiple_choic_multiple_toggle_button', 'select', 'snomed_select', 'organisation_select'
    comparison_date_field_name: string corresponding to field name for date in model
    is_earliest_date: boolean
    earliest_allowable_date: date - used to validate

    It replaces the decorator @update_model as decorators can only redirect the request,
    they cannot pass parameters to the function they wrap. This means that errors raised in updating the model
    cannot be passed back to the template so the logic has been added to this function instead.
    It is important that this function is called early on in the view function and that an updated instance of
    the model AFTER UPDATE is put in the context that is passed back to the template.
    """

    # initialize models
    SyndromeEntity = apps.get_model("epilepsy12", "SyndromeEntity")
    EpilepsyCauseEntity = apps.get_model("epilepsy12", "EpilepsyCauseEntity")
    MedicineEntity = apps.get_model("epilepsy12", "MedicineEntity")
    Registration = apps.get_model("epilepsy12", "Registration")

    if page_element == "toggle_button":
        # toggle button
        # the trigger_name of the element here corresponds to whether true or false has been selected

        if request.htmx.trigger_name == "button-true":
            field_value = True
        elif request.htmx.trigger_name == "button-false":
            field_value = False
        else:
            # an error has occurred
            print("Error has occurred")

    elif (
        page_element == "multiple_choice_multiple_toggle_button"
        or page_element == "single_choice_multiple_toggle_button"
    ):
        # multiple_choice_multiple_toggle_button
        field_value = request.htmx.trigger_name

    elif page_element == "select" or page_element == "snomed_select":
        if request.htmx.trigger_name == "syndrome_name":
            syndrome_entity = SyndromeEntity.objects.get(
                pk=request.POST.get(request.htmx.trigger_name)
            )
            field_value = syndrome_entity  # note field name here is syndrome
        elif request.htmx.trigger_name == "epilepsy_cause":
            epilepsy_cause_entity = EpilepsyCauseEntity.objects.get(
                pk=request.POST.get(request.htmx.trigger_name)
            )
            field_value = (
                epilepsy_cause_entity  # note field name here is epilepsy_cause
            )
        elif request.htmx.trigger_name == "medicine_id":
            medicine_entity = MedicineEntity.objects.get(
                pk=request.POST.get(request.htmx.trigger_name)
            )
            field_value = medicine_entity
            field_name = "medicine_entity"
        else:
            field_value = request.POST.get(request.htmx.trigger_name)

    # validate

    if page_element == "date_field":
        # date tests a bit involved
        # No date can be before the date of birth
        # If a comparison date field is supplied, the date itself might not yet have been set.
        # The earlier of the two dates cannot be in the future and cannot be later than the second if supplied.
        # The later of the two dates CAN be in the future but cannot be earlier than the first if supplied.
        # If there is no comparison date (eg registration_date) the only stipulation is that it not be in the future.
        # This validation step happens in validators.py
        field_value = datetime.strptime(
            request.POST.get(request.htmx.trigger_name), "%Y-%m-%d"
        ).date()

        if is_earliest_date:
            first_date = field_value
            second_date = None
            if comparison_date_field_name:
                instance = model.objects.get(pk=model_id)
                second_date = getattr(instance, comparison_date_field_name)
        else:
            second_date = field_value
            first_date = None
            if comparison_date_field_name:
                instance = model.objects.get(pk=model_id)
                first_date = getattr(instance, comparison_date_field_name)
        epilepsy12_date_validator(
            first_date=first_date,
            second_date=second_date,
            earliest_allowable_date=earliest_allowable_date,
        )

    # update the model

    # if saving a registration_date, this has to trigger the save() method to generate a cohort
    # so update() cannot be used
    # This feels like a bit of a hack so very open to suggestions on more Django way of doing this
    if field_name == "registration_date":
        # registration_date cannot be before date of birth
        registration = Registration.objects.get(pk=model_id)
        if field_value < registration.case.date_of_birth:
            errors = f"The date you chose ({field_value.strftime('%d %B %Y')}) cannot not be before {registration.case}'s date of birth."
            raise ValueError(errors)

        # the registration date cannot be before the current cohort
        current_cohort_end_date = first_tuesday_in_january(
            current_cohort_start_date().year + 2
        ) + relativedelta(days=7)
        if field_value < current_cohort_start_date():
            errors = f'The date you entered cannot be before the current cohort start date ({current_cohort_start_date().strftime("%d %B %Y")})'
            raise ValueError(errors)
        elif field_value > current_cohort_end_date:
            errors = f'The date you entered cannot be after the current cohort end date ({current_cohort_end_date.strftime("%d %B %Y")})'
            raise ValueError(errors)

        else:
            registration = Registration.objects.get(pk=model_id)
            registration.registration_date = field_value
            registration.updated_at = timezone.now()
            registration.updated_by = request.user
            registration.save()
    else:
        updated_field = {
            field_name: field_value,
            "updated_at": timezone.now(),
            "updated_by": request.user,
        }

        try:
            model.objects.filter(pk=model_id).update(**updated_field)
        except DatabaseError as error:
            raise Exception(error)
