from django.db import models
from omop.models.clinical_data import Person

class ConditionEra(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CONDITION_ERA (
			condition_era_id integer NOT NULL,
			person_id integer NOT NULL,
			condition_concept_id integer NOT NULL,
			condition_era_start_date date NOT NULL,
			condition_era_end_date date NOT NULL,
			condition_occurrence_count integer NULL );
    """
    condition_era_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    condition_concept_id = models.IntegerField()
    condition_era_start_date = models.DateField()
    condition_era_end_date = models.DateField()
    condition_occurrence_count = models.IntegerField(null=True, blank=True)


class DrugEra(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.DRUG_ERA (
			drug_era_id integer NOT NULL,
			person_id integer NOT NULL,
			drug_concept_id integer NOT NULL,
			drug_era_start_date date NOT NULL,
			drug_era_end_date date NOT NULL,
			drug_exposure_count integer NULL,
			gap_days integer NULL );
    """
    drug_era_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    drug_concept_id = models.IntegerField()
    drug_era_start_date = models.DateField()
    drug_era_end_date = models.DateField()
    drug_exposure_count = models.IntegerField(null=True, blank=True)
    gap_days = models.IntegerField(null=True, blank=True)

class DoseEra(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.DOSE_ERA (
			dose_era_id integer NOT NULL,
			person_id integer NOT NULL,
			drug_concept_id integer NOT NULL,
			unit_concept_id integer NOT NULL,
			dose_value NUMERIC NOT NULL,
			dose_era_start_date date NOT NULL,
			dose_era_end_date date NOT NULL );
    """
    dose_era_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    drug_concept_id = models.IntegerField()
    unit_concept_id = models.IntegerField()
    dose_value = models.DecimalField(max_digits=10, decimal_places=2)
    dose_era_start_date = models.DateField()
    dose_era_end_date = models.DateField()


class Cohort(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.COHORT (
			cohort_definition_id integer NOT NULL,
			subject_id integer NOT NULL,
			cohort_start_date date NOT NULL,
			cohort_end_date date NOT NULL );
    """
    cohort_definition_id = models.IntegerField(primary_key=True)
    subject_id = models.IntegerField()
    cohort_start_date = models.DateField()
    cohort_end_date = models.DateField()


class CohortDefinition(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.COHORT_DEFINITION (
			cohort_definition_id integer NOT NULL,
			cohort_definition_name varchar(255) NOT NULL,
			cohort_definition_description TEXT NULL,
			definition_type_concept_id integer NOT NULL,
			cohort_definition_syntax TEXT NULL,
			subject_concept_id integer NOT NULL,
			cohort_initiation_date date NULL );
    """
    cohort_definition_id = models.IntegerField(primary_key=True)
    cohort_definition_name = models.CharField(max_length=255)
    cohort_definition_description = models.TextField(null=True, blank=True)
    definition_type_concept_id = models.IntegerField()
    cohort_definition_syntax = models.TextField(null=True, blank=True)
    subject_concept_id = models.IntegerField()
    cohort_initiation_date = models.DateField(null=True, blank=True)

