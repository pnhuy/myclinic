from django.db import models
from omop.models import DEFAULT_ON_DELETE
from omop.models.health_system import CareSite, Location, Provider
from omop.models.vocabularies import Concept

class Person(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.PERSON (
			person_id integer NOT NULL,
			gender_concept_id integer NOT NULL,
			year_of_birth integer NOT NULL,
			month_of_birth integer NULL,
			day_of_birth integer NULL,
			birth_datetime TIMESTAMP NULL,
			race_concept_id integer NOT NULL,
			ethnicity_concept_id integer NOT NULL,
			location_id integer NULL,
			provider_id integer NULL,
			care_site_id integer NULL,
			person_source_value varchar(50) NULL,
			gender_source_value varchar(50) NULL,
			gender_source_concept_id integer NULL,
			race_source_value varchar(50) NULL,
			race_source_concept_id integer NULL,
			ethnicity_source_value varchar(50) NULL,
			ethnicity_source_concept_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.PERSON ADD CONSTRAINT xpk_PERSON PRIMARY KEY (person_id);
    """
    person_id = models.IntegerField(primary_key=True)
    gender_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='person_gender_concept_ids')
    year_of_birth = models.IntegerField()
    month_of_birth = models.IntegerField(null=True, blank=True)
    day_of_birth = models.IntegerField(null=True, blank=True)
    birth_datetime = models.DateTimeField(null=True, blank=True)
    race_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='race_concept_ids')
    ethnicity_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='ethnicity_concept_ids')
    location_id = models.ForeignKey(Location, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    care_site_id = models.ForeignKey(CareSite, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    person_source_value = models.CharField(max_length=50, null=True, blank=True)
    gender_source_value = models.CharField(max_length=50, null=True, blank=True)
    gender_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='gender_source_concept_id')
    race_source_value = models.CharField(max_length=50, null=True, blank=True)
    race_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='race_source_concept_ids')
    ethnicity_source_value = models.CharField(max_length=50, null=True, blank=True)
    ethnicity_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='ethnicity_source_concept_ids')


class ObservationPeriod(models.Model):
    """CREATE TABLE @cdmDatabaseSchema.OBSERVATION_PERIOD (
			observation_period_id integer NOT NULL,
			person_id integer NOT NULL,
			observation_period_start_date date NOT NULL,
			observation_period_end_date date NOT NULL,
			period_type_concept_id integer NOT NULL );
    ALTER TABLE @cdmDatabaseSchema.OBSERVATION_PERIOD ADD CONSTRAINT xpk_OBSERVATION_PERIOD PRIMARY KEY (observation_period_id);
    """
    observation_period_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    observation_period_start_date = models.DateField()
    observation_period_end_date = models.DateField()
    period_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE)



class Death(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.DEATH (
			person_id integer NOT NULL,
			death_date date NOT NULL,
			death_datetime TIMESTAMP NULL,
			death_type_concept_id integer NULL,
			cause_concept_id integer NULL,
			cause_source_value varchar(50) NULL,
			cause_source_concept_id integer NULL );
    """
    person_id = models.OneToOneField(Person, on_delete=DEFAULT_ON_DELETE, primary_key=True)
    death_date = models.DateField()
    death_datetime = models.DateTimeField(null=True, blank=True)
    death_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='death_type_concept_ids')
    cause_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='cause_concept_ids')
    cause_source_value = models.CharField(max_length=50, null=True, blank=True)
    cause_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='cause_source_concept_ids')



class VisitOccurrence(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.VISIT_OCCURRENCE (
			visit_occurrence_id integer NOT NULL,
			person_id integer NOT NULL,
			visit_concept_id integer NOT NULL,
			visit_start_date date NOT NULL,
			visit_start_datetime TIMESTAMP NULL,
			visit_end_date date NOT NULL,
			visit_end_datetime TIMESTAMP NULL,
			visit_type_concept_id Integer NOT NULL,
			provider_id integer NULL,
			care_site_id integer NULL,
			visit_source_value varchar(50) NULL,
			visit_source_concept_id integer NULL,
			admitted_from_concept_id integer NULL,
			admitted_from_source_value varchar(50) NULL,
			discharged_to_concept_id integer NULL,
			discharged_to_source_value varchar(50) NULL,
			preceding_visit_occurrence_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.VISIT_OCCURRENCE ADD CONSTRAINT xpk_VISIT_OCCURRENCE PRIMARY KEY (visit_occurrence_id);
    """
    visit_occurrence_id = models.IntegerField(primary_key=True)

    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    visit_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='visit_concept_ids')
    visit_start_date = models.DateField()
    visit_start_datetime = models.DateTimeField(null=True, blank=True)
    visit_end_date = models.DateField()
    visit_end_datetime = models.DateTimeField(null=True, blank=True)
    visit_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='visit_type_concept_ids')
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    care_site_id = models.ForeignKey(CareSite, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_source_value = models.CharField(max_length=50, null=True, blank=True)
    visit_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='visit_source_concept_ids')
    admitted_from_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='visit_occurence_admitted_from_concept_ids')
    admitted_from_source_value = models.CharField(max_length=50, null=True, blank=True)
    discharged_to_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='visit_occurence_discharged_to_concept_ids')
    discharged_to_source_value = models.CharField(max_length=50, null=True, blank=True)
    preceding_visit_occurrence_id = models.ForeignKey('self', on_delete=DEFAULT_ON_DELETE, null=True, blank=True)



class VisitDetail(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.VISIT_DETAIL (
			visit_detail_id integer NOT NULL,
			person_id integer NOT NULL,
			visit_detail_concept_id integer NOT NULL,
			visit_detail_start_date date NOT NULL,
			visit_detail_start_datetime TIMESTAMP NULL,
			visit_detail_end_date date NOT NULL,
			visit_detail_end_datetime TIMESTAMP NULL,
			visit_detail_type_concept_id integer NOT NULL,
			provider_id integer NULL,
			care_site_id integer NULL,
			visit_detail_source_value varchar(50) NULL,
			visit_detail_source_concept_id Integer NULL,
			admitted_from_concept_id Integer NULL,
			admitted_from_source_value varchar(50) NULL,
			discharged_to_source_value varchar(50) NULL,
			discharged_to_concept_id integer NULL,
			preceding_visit_detail_id integer NULL,
			parent_visit_detail_id integer NULL,
			visit_occurrence_id integer NOT NULL );
    ALTER TABLE @cdmDatabaseSchema.VISIT_DETAIL ADD CONSTRAINT xpk_VISIT_DETAIL PRIMARY KEY (visit_detail_id);
    """
    visit_detail_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    visit_detail_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='visit_detail_concept_ids')
    visit_detail_start_date = models.DateField()
    visit_detail_start_datetime = models.DateTimeField(null=True, blank=True)
    visit_detail_end_date = models.DateField()
    visit_detail_end_datetime = models.DateTimeField(null=True, blank=True)
    visit_detail_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='visit_detail_type_concept_ids')
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    care_site_id = models.ForeignKey(CareSite, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_detail_source_value = models.CharField(max_length=50, null=True, blank=True)
    visit_detail_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='visit_detail_source_concept_ids')
    admitted_from_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='visit_detail_admitted_from_concept_ids')
    admitted_from_source_value = models.CharField(max_length=50, null=True, blank=True)
    discharged_to_source_value = models.CharField(max_length=50, null=True, blank=True)
    discharged_to_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='visit_detail_discharged_to_concept_ids')
    preceding_visit_detail_id = models.ForeignKey('self', on_delete=DEFAULT_ON_DELETE, related_name="following_visit_detail", null=True, blank=True)
    parent_visit_detail_id = models.ForeignKey('self', on_delete=DEFAULT_ON_DELETE, related_name="child_visit_detail", null=True, blank=True)
    visit_occurrence_id = models.ForeignKey(VisitOccurrence, on_delete=DEFAULT_ON_DELETE)


class ConditionOccurrence(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CONDITION_OCCURRENCE (
			condition_occurrence_id integer NOT NULL,
			person_id integer NOT NULL,
			condition_concept_id integer NOT NULL,
			condition_start_date date NOT NULL,
			condition_start_datetime TIMESTAMP NULL,
			condition_end_date date NULL,
			condition_end_datetime TIMESTAMP NULL,
			condition_type_concept_id integer NOT NULL,
			condition_status_concept_id integer NULL,
			stop_reason varchar(20) NULL,
			provider_id integer NULL,
			visit_occurrence_id integer NULL,
			visit_detail_id integer NULL,
			condition_source_value varchar(50) NULL,
			condition_source_concept_id integer NULL,
			condition_status_source_value varchar(50) NULL );
    ALTER TABLE @cdmDatabaseSchema.CONDITION_OCCURRENCE ADD CONSTRAINT xpk_CONDITION_OCCURRENCE PRIMARY KEY (condition_occurrence_id);
    """
    condition_occurrence_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    condition_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='condition_concept_ids')
    condition_start_date = models.DateField()
    condition_start_datetime = models.DateTimeField(null=True, blank=True)
    condition_end_date = models.DateField(null=True, blank=True)
    condition_end_datetime = models.DateTimeField(null=True, blank=True)
    condition_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='condition_type_concept_ids')
    condition_status_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='condition_status_concept_ids')
    stop_reason = models.CharField(max_length=20, null=True, blank=True)
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_occurrence_id = models.ForeignKey(VisitOccurrence, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_detail_id = models.ForeignKey(VisitDetail, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    condition_source_value = models.CharField(max_length=50, null=True, blank=True)
    condition_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='condition_source_concept_ids')
    condition_status_source_value = models.CharField(max_length=50, null=True, blank=True)


class DrugExposure(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.DRUG_EXPOSURE (
			drug_exposure_id integer NOT NULL,
			person_id integer NOT NULL,
			drug_concept_id integer NOT NULL,
			drug_exposure_start_date date NOT NULL,
			drug_exposure_start_datetime TIMESTAMP NULL,
			drug_exposure_end_date date NOT NULL,
			drug_exposure_end_datetime TIMESTAMP NULL,
			verbatim_end_date date NULL,
			drug_type_concept_id integer NOT NULL,
			stop_reason varchar(20) NULL,
			refills integer NULL,
			quantity NUMERIC NULL,
			days_supply integer NULL,
			sig TEXT NULL,
			route_concept_id integer NULL,
			lot_number varchar(50) NULL,
			provider_id integer NULL,
			visit_occurrence_id integer NULL,
			visit_detail_id integer NULL,
			drug_source_value varchar(50) NULL,
			drug_source_concept_id integer NULL,
			route_source_value varchar(50) NULL,
			dose_unit_source_value varchar(50) NULL );
    ALTER TABLE @cdmDatabaseSchema.DRUG_EXPOSURE ADD CONSTRAINT xpk_DRUG_EXPOSURE PRIMARY KEY (drug_exposure_id);
    """
    drug_exposure_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    drug_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='drug_exposure_drug_concept_ids')
    drug_exposure_start_date = models.DateField()
    drug_exposure_start_datetime = models.DateTimeField(null=True, blank=True)
    drug_exposure_end_date = models.DateField()
    drug_exposure_end_datetime = models.DateTimeField(null=True, blank=True)
    verbatim_end_date = models.DateField(null=True, blank=True)
    drug_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='drug_type_concept_ids')
    stop_reason = models.CharField(max_length=20, null=True, blank=True)
    refills = models.IntegerField(null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    days_supply = models.IntegerField(null=True, blank=True)
    sig = models.TextField(null=True, blank=True)
    route_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='route_concept_ids')
    lot_number = models.CharField(max_length=50, null=True, blank=True)
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_occurrence_id = models.ForeignKey(VisitOccurrence, on_delete=models.CASCADE, null=True, blank=True)
    visit_detail_id = models.ForeignKey(VisitDetail, on_delete=models.CASCADE, null=True, blank=True)
    drug_source_value = models.CharField(max_length=50, null=True, blank=True)
    drug_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='drug_source_concept_ids')
    route_source_value = models.CharField(max_length=50, null=True, blank=True)
    dose_unit_source_value = models.CharField(max_length=50, null=True, blank=True)


class ProcedureOccurrence(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.PROCEDURE_OCCURRENCE (
			procedure_occurrence_id integer NOT NULL,
			person_id integer NOT NULL,
			procedure_concept_id integer NOT NULL,
			procedure_date date NOT NULL,
			procedure_datetime TIMESTAMP NULL,
			procedure_end_date date NULL,
			procedure_end_datetime TIMESTAMP NULL,
			procedure_type_concept_id integer NOT NULL,
			modifier_concept_id integer NULL,
			quantity integer NULL,
			provider_id integer NULL,
			visit_occurrence_id integer NULL,
			visit_detail_id integer NULL,
			procedure_source_value varchar(50) NULL,
			procedure_source_concept_id integer NULL,
			modifier_source_value varchar(50) NULL );
    ALTER TABLE @cdmDatabaseSchema.PROCEDURE_OCCURRENCE ADD CONSTRAINT xpk_PROCEDURE_OCCURRENCE PRIMARY KEY (procedure_occurrence_id);
    """
    procedure_occurrence_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    procedure_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='procedure_concept_ids')
    procedure_date = models.DateField()
    procedure_datetime = models.DateTimeField(null=True, blank=True)
    procedure_end_date = models.DateField(null=True, blank=True)
    procedure_end_datetime = models.DateTimeField(null=True, blank=True)
    procedure_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='procedure_type_concept_ids')
    modifier_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='modifier_concept_ids')
    quantity = models.IntegerField(null=True, blank=True)
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_occurrence_id = models.ForeignKey(VisitOccurrence, on_delete=models.CASCADE, null=True, blank=True)
    visit_detail_id = models.ForeignKey(VisitDetail, on_delete=models.CASCADE, null=True, blank=True)
    procedure_source_value = models.CharField(max_length=50, null=True, blank=True)
    procedure_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='procedure_source_concept_ids')
    modifier_source_value = models.CharField(max_length=50, null=True, blank=True)

class DeviceExposure(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.DEVICE_EXPOSURE (
			device_exposure_id integer NOT NULL,
			person_id integer NOT NULL,
			device_concept_id integer NOT NULL,
			device_exposure_start_date date NOT NULL,
			device_exposure_start_datetime TIMESTAMP NULL,
			device_exposure_end_date date NULL,
			device_exposure_end_datetime TIMESTAMP NULL,
			device_type_concept_id integer NOT NULL,
			unique_device_id varchar(255) NULL,
			production_id varchar(255) NULL,
			quantity integer NULL,
			provider_id integer NULL,
			visit_occurrence_id integer NULL,
			visit_detail_id integer NULL,
			device_source_value varchar(50) NULL,
			device_source_concept_id integer NULL,
			unit_concept_id integer NULL,
			unit_source_value varchar(50) NULL,
			unit_source_concept_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.DEVICE_EXPOSURE ADD CONSTRAINT xpk_DEVICE_EXPOSURE PRIMARY KEY (device_exposure_id);
    """
    device_exposure_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    device_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='device_concept_ids')
    device_exposure_start_date = models.DateField()
    device_exposure_start_datetime = models.DateTimeField(null=True, blank=True)
    device_exposure_end_date = models.DateField(null=True, blank=True)
    device_exposure_end_datetime = models.DateTimeField(null=True, blank=True)
    device_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='device_type_concept_ids')
    unique_device_id = models.CharField(max_length=255, null=True, blank=True)
    production_id = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_occurrence_id = models.ForeignKey(VisitOccurrence, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_detail_id = models.ForeignKey(VisitDetail, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    device_source_value = models.CharField(max_length=50, null=True, blank=True)
    device_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='device_source_concept_ids')
    unit_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='device_exposure_unit_concept_ids')
    unit_source_value = models.CharField(max_length=50, null=True, blank=True)
    unit_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='device_exposure_unit_source_concept_ids')

class Measurement(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.MEASUREMENT (
			measurement_id integer NOT NULL,
			person_id integer NOT NULL,
			measurement_concept_id integer NOT NULL,
			measurement_date date NOT NULL,
			measurement_datetime TIMESTAMP NULL,
			measurement_time varchar(10) NULL,
			measurement_type_concept_id integer NOT NULL,
			operator_concept_id integer NULL,
			value_as_number NUMERIC NULL,
			value_as_concept_id integer NULL,
			unit_concept_id integer NULL,
			range_low NUMERIC NULL,
			range_high NUMERIC NULL,
			provider_id integer NULL,
			visit_occurrence_id integer NULL,
			visit_detail_id integer NULL,
			measurement_source_value varchar(50) NULL,
			measurement_source_concept_id integer NULL,
			unit_source_value varchar(50) NULL,
			unit_source_concept_id integer NULL,
			value_source_value varchar(50) NULL,
			measurement_event_id integer NULL,
			meas_event_field_concept_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.MEASUREMENT ADD CONSTRAINT xpk_MEASUREMENT PRIMARY KEY (measurement_id);
    """
    measurement_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    measurement_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='measurement_concept_ids')
    measurement_date = models.DateField()
    measurement_datetime = models.DateTimeField(null=True, blank=True)
    measurement_time = models.CharField(max_length=10, null=True, blank=True)
    measurement_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='measurement_type_concept_ids')
    operator_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='operator_concept_ids')
    value_as_number = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    value_as_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='measurement_value_as_concept_ids')
    unit_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='measurement_unit_concept_ids')
    range_low = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    range_high = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_occurrence_id = models.ForeignKey(VisitOccurrence, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_detail_id = models.ForeignKey(VisitDetail, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    measurement_source_value = models.CharField(max_length=50, null=True, blank=True)
    measurement_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='measurement_source_concept_ids')
    unit_source_value = models.CharField(max_length=50, null=True, blank=True)
    unit_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='unit_source_concept_ids')
    value_source_value = models.CharField(max_length=50, null=True, blank=True)
    measurement_event_id = models.IntegerField(null=True, blank=True)
    meas_event_field_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='meas_event_field_concept_ids')


class Observation(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.OBSERVATION (
			observation_id integer NOT NULL,
			person_id integer NOT NULL,
			observation_concept_id integer NOT NULL,
			observation_date date NOT NULL,
			observation_datetime TIMESTAMP NULL,
			observation_type_concept_id integer NOT NULL,
			value_as_number NUMERIC NULL,
			value_as_string varchar(60) NULL,
			value_as_concept_id Integer NULL,
			qualifier_concept_id integer NULL,
			unit_concept_id integer NULL,
			provider_id integer NULL,
			visit_occurrence_id integer NULL,
			visit_detail_id integer NULL,
			observation_source_value varchar(50) NULL,
			observation_source_concept_id integer NULL,
			unit_source_value varchar(50) NULL,
			qualifier_source_value varchar(50) NULL,
			value_source_value varchar(50) NULL,
			observation_event_id integer NULL,
			obs_event_field_concept_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.OBSERVATION ADD CONSTRAINT xpk_OBSERVATION PRIMARY KEY (observation_id);
    """
    observation_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    observation_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='observation_concept_ids')
    observation_date = models.DateField()
    observation_datetime = models.DateTimeField(null=True, blank=True)
    observation_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='observation_type_concept_ids')
    value_as_number = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    value_as_string = models.CharField(max_length=60, null=True, blank=True)
    value_as_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='observation_value_as_concept_ids')
    qualifier_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='qualifier_concept_ids')
    unit_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='observation_unit_concept_ids')
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_occurrence_id = models.ForeignKey(VisitOccurrence, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_detail_id = models.ForeignKey(VisitDetail, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    observation_source_value = models.CharField(max_length=50, null=True, blank=True)
    observation_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE,null=True, blank=True, related_name='observation_source_concept_ids')
    unit_source_value = models.CharField(max_length=50, null=True, blank=True)
    qualifier_source_value = models.CharField(max_length=50, null=True, blank=True)
    value_source_value = models.CharField(max_length=50, null=True, blank=True)
    observation_event_id = models.IntegerField(null=True, blank=True)
    obs_event_field_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='obs_event_field_concept_ids')

class Note(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.NOTE (
			note_id integer NOT NULL,
			person_id integer NOT NULL,
			note_date date NOT NULL,
			note_datetime TIMESTAMP NULL,
			note_type_concept_id integer NOT NULL,
			note_class_concept_id integer NOT NULL,
			note_title varchar(250) NULL,
			note_text TEXT NOT NULL,
			encoding_concept_id integer NOT NULL,
			language_concept_id integer NOT NULL,
			provider_id integer NULL,
			visit_occurrence_id integer NULL,
			visit_detail_id integer NULL,
			note_source_value varchar(50) NULL,
			note_event_id integer NULL,
			note_event_field_concept_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.NOTE ADD CONSTRAINT xpk_NOTE PRIMARY KEY (note_id);
    """
    note_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    note_date = models.DateField()
    note_datetime = models.DateTimeField(null=True, blank=True)
    note_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='note_type_concept_ids')
    note_class_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='note_class_concept_ids')
    note_title = models.CharField(max_length=250, null=True, blank=True)
    note_text = models.TextField()
    encoding_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='encoding_concept_ids')
    language_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='note_language_concept_ids')
    provider_id = models.ForeignKey(Provider, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_occurrence_id = models.ForeignKey(VisitOccurrence, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    visit_detail_id = models.ForeignKey(VisitDetail, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    note_source_value = models.CharField(max_length=50, null=True, blank=True)
    note_event_id = models.IntegerField(null=True, blank=True)
    note_event_field_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='note_note_event_field_concept_ids')


class NoteNlp(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.NOTE_NLP (
			note_nlp_id integer NOT NULL,
			note_id integer NOT NULL,
			section_concept_id integer NULL,
			snippet varchar(250) NULL,
			"offset" varchar(50) NULL,
			lexical_variant varchar(250) NOT NULL,
			note_nlp_concept_id integer NULL,
			note_nlp_source_concept_id integer NULL,
			nlp_system varchar(250) NULL,
			nlp_date date NOT NULL,
			nlp_datetime TIMESTAMP NULL,
			term_exists varchar(1) NULL,
			term_temporal varchar(50) NULL,
			term_modifiers varchar(2000) NULL );
    ALTER TABLE @cdmDatabaseSchema.NOTE_NLP ADD CONSTRAINT xpk_NOTE_NLP PRIMARY KEY (note_nlp_id);
    """
    note_nlp_id = models.IntegerField(primary_key=True)
    note_id = models.ForeignKey(Note, on_delete=DEFAULT_ON_DELETE) # Different from CDM 5.4 Constraints
    section_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='section_concept_ids')
    snippet = models.CharField(max_length=250, null=True, blank=True)
    offset = models.CharField(max_length=50, null=True, blank=True)
    lexical_variant = models.CharField(max_length=250)
    note_nlp_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='note_nlp_concept_ids')
    note_nlp_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='note_nlp_source_concept_ids')
    nlp_system = models.CharField(max_length=250, null=True, blank=True)
    nlp_date = models.DateField()
    nlp_datetime = models.DateTimeField(null=True, blank=True)
    term_exists = models.CharField(max_length=1, null=True, blank=True)
    term_temporal = models.CharField(max_length=50, null=True, blank=True)
    term_modifiers = models.CharField(max_length=2000, null=True, blank=True)

class Episode(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.EPISODE (
			episode_id integer NOT NULL,
			person_id integer NOT NULL,
			episode_concept_id integer NOT NULL,
			episode_start_date date NOT NULL,
			episode_start_datetime TIMESTAMP NULL,
			episode_end_date date NULL,
			episode_end_datetime TIMESTAMP NULL,
			episode_parent_id integer NULL,
			episode_number integer NULL,
			episode_object_concept_id integer NOT NULL,
			episode_type_concept_id integer NOT NULL,
			episode_source_value varchar(50) NULL,
			episode_source_concept_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.EPISODE ADD CONSTRAINT xpk_EPISODE PRIMARY KEY (episode_id);
    """
    episode_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    episode_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='episode_concept_ids')
    episode_start_date = models.DateField()
    episode_start_datetime = models.DateTimeField(null=True, blank=True)
    episode_end_date = models.DateField(null=True, blank=True)
    episode_end_datetime = models.DateTimeField(null=True, blank=True)
    episode_parent_id = models.ForeignKey('self', on_delete=DEFAULT_ON_DELETE, null=True, blank=True) # Different
    episode_number = models.IntegerField(null=True, blank=True)
    episode_object_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='episode_object_concept_ids')
    episode_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='episode_type_concept_ids')
    episode_source_value = models.CharField(max_length=50, null=True, blank=True)
    episode_source_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='episode_source_concept_ids')


class EpisodeEvent(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.EPISODE_EVENT (
			episode_id integer NOT NULL,
			event_id integer NOT NULL,
			episode_event_field_concept_id integer NOT NULL );
    """
    episode_id = models.ForeignKey(Episode, on_delete=DEFAULT_ON_DELETE)
    event_id = models.IntegerField()
    episode_event_field_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE)

class Specimen(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.SPECIMEN (
			specimen_id integer NOT NULL,
			person_id integer NOT NULL,
			specimen_concept_id integer NOT NULL,
			specimen_type_concept_id integer NOT NULL,
			specimen_date date NOT NULL,
			specimen_datetime TIMESTAMP NULL,
			quantity NUMERIC NULL,
			unit_concept_id integer NULL,
			anatomic_site_concept_id integer NULL,
			disease_status_concept_id integer NULL,
			specimen_source_id varchar(50) NULL,
			specimen_source_value varchar(50) NULL,
			unit_source_value varchar(50) NULL,
			anatomic_site_source_value varchar(50) NULL,
			disease_status_source_value varchar(50) NULL );
    ALTER TABLE @cdmDatabaseSchema.SPECIMEN ADD CONSTRAINT xpk_SPECIMEN PRIMARY KEY (specimen_id);
    """
    specimen_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    specimen_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='specimen_concept_ids')
    specimen_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='specimen_type_concept_ids')
    specimen_date = models.DateField()
    specimen_datetime = models.DateTimeField(null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='specimen_unit_concept_ids')
    anatomic_site_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='anatomic_site_concept_ids')
    disease_status_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='disease_status_concept_ids')
    specimen_source_id = models.CharField(max_length=50, null=True, blank=True)
    specimen_source_value = models.CharField(max_length=50, null=True, blank=True)
    unit_source_value = models.CharField(max_length=50, null=True, blank=True)
    anatomic_site_source_value = models.CharField(max_length=50, null=True, blank=True)
    disease_status_source_value = models.CharField(max_length=50, null=True, blank=True)


class FactRelationship(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.FACT_RELATIONSHIP (
			domain_concept_id_1 integer NOT NULL,
			fact_id_1 integer NOT NULL,
			domain_concept_id_2 integer NOT NULL,
			fact_id_2 integer NOT NULL,
			relationship_concept_id integer NOT NULL );
    """
    domain_concept_id_1 = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='domain_concept_id_1s')
    fact_id_1 = models.IntegerField()
    domain_concept_id_2 = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='domain_concept_id_2s')
    fact_id_2 = models.IntegerField()
    relationship_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='relationship_concept_ids')
