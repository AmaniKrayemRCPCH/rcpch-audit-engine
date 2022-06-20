from . import views
from .view_folder import HospitalAutocomplete
from .view_folder import SemiologyKeywordAutocomplete
from .views import SignUpView
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('database', views.database, name="database"),
    path('hospital', views.hospital_reports, name="hospital_reports"),
    path('cases', views.case_list, name="cases"),
    path('case/<int:id>/update', views.update_case, name="update_case"),
    path('case/create', views.create_case, name="create_case"),
    path('case/<int:id>/delete', views.delete_case, name="delete_case"),
    path('case/<int:id>/register',
         views.register, name='register'),
    path('registration/<int:id>/update',
         views.update_registration, name="update_registration"),
    path('initial_assessment/<int:case_id>/create',
         views.create_initial_assessment, name="create_initial_assessment"),
    path('initial_assessment/<int:case_id>/update',
         views.update_initial_assessment, name="update_initial_assessment"),
    path('assessment/<int:case_id>/create',
         views.create_assessment, name="create_assessment"),
    path('assessment/<int:case_id>/update',
         views.update_assessment, name="update_assessment"),
    path('multiaxial_description/<int:case_id>',
         views.multiaxial_description, name='multiaxial_description'),
    path('epilepsy_context/<int:case_id>/create',
         views.create_epilepsy_context, name='create_epilepsy_context'),
    path('epilepsy_context/<int:case_id>/update',
         views.update_epilepsy_context, name='update_epilepsy_context'),
    path('comorbidity/<int:case_id>/create',
         views.create_comorbidity, name="create_comorbidity"),
    path('comorbidity/<int:case_id>/update',
         views.update_comorbidity, name="update_comorbidity"),
    path('investigation_management/<int:case_id>/create',
         views.create_investigation_management, name='create_investigation_management'),
    path('investigation_management/<int:case_id>/update',
         views.update_investigation_management, name='update_investigation_management'),
    path('eeg', views.eeg, name="eeg"),
    path('patient', views.patient, name="patient"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('hospital-autocomplete/', HospitalAutocomplete.as_view(),
         name='hospital-autocomplete'),
    path('semiology-keyword-autocomplete/', SemiologyKeywordAutocomplete.as_view(),
         name='semiology-keyword-autocomplete'),
]

htmx_paths = [
    path('htmx/<int:desscribe_id>/description',
         views.edit_description, name='edit_description'),
    path('htmx/<int:desscribe_id>/description_keyword/<int:description_keyword_id>/delete',
         views.delete_description_keyword, name='delete_description_keyword'),
    path('htmx/<int:desscribe_id>/epilepsy_or_nonepilepsy_status_changed',
         views.epilepsy_or_nonepilepsy_status_changed, name='epilepsy_or_nonepilepsy_status_changed'),
    path('htmx/<int:desscribe_id>/epilepsy_onset_changed',
         views.epilepsy_onset_changed, name='epilepsy_onset_changed'),
    path('htmx/<int:desscribe_id>/focal_onset_epilepsy_checked_changed',
         views.focal_onset_epilepsy_checked_changed, name='focal_onset_epilepsy_checked_changed'),
    path('htmx/<int:desscribe_id>/nonepilepsy_generalised_onset',
         views.nonepilepsy_generalised_onset, name='nonepilepsy_generalised_onset'),
    path('htmx/<int:desscribe_id>/nonepilepsy_generalised_onset_edit',
         views.nonepilepsy_generalised_onset_edit, name='nonepilepsy_generalised_onset_edit'),
    path('htmx/<int:desscribe_id>/nonepilepsy_subtypes',
         views.nonepilepsy_subtypes, name='nonepilepsy_subtypes'),
    path('htmx/<int:desscribe_id>/nonepilepsy_subtype_selection/<str:nonepilepsy_selected_subtype_code>',
         views.nonepilepsy_subtype_selection, name='nonepilepsy_subtype_selection'),
    path('htmx/<int:desscribe_id>/syndrome_select',
         views.syndrome_select, name='syndrome_select'),
    path('htmx/<int:desscribe_id>/seizure_cause_main',
         views.seizure_cause_main, name='seizure_cause_main'),
    path('htmx/<int:desscribe_id>/seizure_cause_main/<str:seizure_cause_main>',
         views.seizure_cause_main_choice, name='seizure_cause_main_choice'),
    path('htmx/<int:desscribe_id>/seizure_cause_infectious',
         views.seizure_cause_infectious, name='seizure_cause_infectious'),
    path('htmx/<int:desscribe_id>/genetic_selection',
         views.seizure_cause_genetic_choice, name='seizure_cause_genetic_choice'),
    path('htmx/<int:desscribe_id>/autoantibodies',
         views.autoantibodies, name='autoantibodies'),
    path('htmx/<int:desscribe_id>/ribe',
         views.ribe, name='ribe'),
    path('htmx/filter_case_list', views.case_list,
         name="filter_case_list"),

]

urlpatterns += htmx_paths
