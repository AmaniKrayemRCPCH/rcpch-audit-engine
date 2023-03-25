from datetime import date
from dateutil.relativedelta import relativedelta
from django import forms
from django.forms import ValidationError
from ..models import Case
from ..constants import *
from ..general_functions import is_valid_postcode, validate_nhs_number


class CaseForm(forms.ModelForm):
    unknown_postcode = forms.CharField()

    first_name = forms.CharField(
        help_text="Enter the first name.",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "first name"
            }
        )
    )
    surname = forms.CharField(
        help_text="Enter the surname.",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "surname"
            }
        )
    )
    date_of_birth = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "date of birth",
                "type": "date"
            }
        )
    )
    sex = forms.ChoiceField(
        choices=SEX_TYPE,
        widget=forms.Select(attrs={'class': 'ui rcpch dropdown'}),
        required=True
    )
    nhs_number = forms.CharField(
        help_text="Enter the NHS Number. This is 10 digits long.",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "NHS Number",
                "type": "text"
            }
        ),
        required=True
    )
    postcode = forms.CharField(
        help_text="Enter the postcode.",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Postcode",
                "type": "text"
            }
        ),
        required=True
    )
    ethnicity = forms.ChoiceField(
        choices=ETHNICITIES,
        widget=forms.Select(
            attrs={
                'class': 'ui rcpch dropdown'
            }
        ),
        required=True
    )
    locked_at = forms.DateTimeField(
        help_text="Time record locked.",
        required=False
    )
    locked_by = forms.CharField(
        help_text="User who locked the record",
        required=False
    )

    def __init__(self, *args, **kwargs) -> None:
        super(CaseForm, self).__init__(*args, **kwargs)
        self.fields['ethnicity'].widget.attrs.update({
            'class': 'ui rcpch dropdown'
        })
        self.existing_nhs_number = int(self.instance.nhs_number)

    class Meta:
        model = Case
        fields = [
            'first_name', 'surname', 'date_of_birth', 'sex', 'nhs_number', 'postcode', 'ethnicity', 'unknown_postcode'
        ]

    # def clean(self):
    #     cleaned_data = super(CaseForm, self).clean()

    #     return cleaned_data
    def clean_postcode(self):
        postcode = self.cleaned_data['postcode']
        if is_valid_postcode(postcode=postcode):
            return postcode
        else:
            raise ValidationError('Invalid postcode')

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        today = date.today()
        if date_of_birth > today:
            raise ValidationError("Date of birth cannot be in the future.")
        else:
            return date_of_birth

    def clean_nhs_number(self):
        # remove spaces
        nhs_number = self.cleaned_data['nhs_number']
        formatted_number = int(str(nhs_number).replace(' ', ''))

        # ensure NHS number is unique in the database
        if self.existing_nhs_number is not None:
            # this form is updating an existing NHS number
            if formatted_number != self.existing_nhs_number:
                # the new number does not match the one stored
                if Case.objects.filter(nhs_number=formatted_number).exists():
                    raise ValidationError('NHS Number already taken!')
        else:
            # this is a new form - check this number is unique in the database
            if Case.objects.filter(nhs_number=formatted_number).exists():
                raise ValidationError('NHS Number already taken!')
        validity = validate_nhs_number(nhs_number)
        if validity['valid']:
            return nhs_number
        else:
            raise ValidationError(validity['message'])
