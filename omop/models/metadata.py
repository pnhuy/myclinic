from django.db import models
from omop.models import DEFAULT_ON_DELETE

from omop.models.vocabularies import Concept

class Metadata(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.METADATA (
			metadata_id integer NOT NULL,
			metadata_concept_id integer NOT NULL,
			metadata_type_concept_id integer NOT NULL,
			name varchar(250) NOT NULL,
			value_as_string varchar(250) NULL,
			value_as_concept_id integer NULL,
			value_as_number NUMERIC NULL,
			metadata_date date NULL,
			metadata_datetime TIMESTAMP NULL );
    ALTER TABLE @cdmDatabaseSchema.METADATA ADD CONSTRAINT xpk_METADATA PRIMARY KEY (metadata_id);
    """
    metadata_id = models.IntegerField(primary_key=True)
    metadata_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='metadata_concept_ids')
    metadata_type_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, related_name='metadata_type_concept_id')
    name = models.CharField(max_length=250)
    value_as_string = models.CharField(max_length=250, null=True, blank=True)
    value_as_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True, related_name='value_as_concept_ids')
    value_as_number = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    metadata_date = models.DateField(null=True, blank=True)
    metadata_datetime = models.DateTimeField(null=True, blank=True)


class CdmSource(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CDM_SOURCE (
			cdm_source_name varchar(255) NOT NULL,
			cdm_source_abbreviation varchar(25) NOT NULL,
			cdm_holder varchar(255) NOT NULL,
			source_description TEXT NULL,
			source_documentation_reference varchar(255) NULL,
			cdm_etl_reference varchar(255) NULL,
			source_release_date date NOT NULL,
			cdm_release_date date NOT NULL,
			cdm_version varchar(10) NULL,
			cdm_version_concept_id integer NOT NULL,
			vocabulary_version varchar(20) NOT NULL );
    """
    cdm_source_name = models.CharField(max_length=255)
    cdm_source_abbreviation = models.CharField(max_length=25)
    cdm_holder = models.CharField(max_length=255)
    source_description = models.TextField(null=True, blank=True)
    source_documentation_reference = models.CharField(max_length=255, null=True, blank=True)
    cdm_etl_reference = models.CharField(max_length=255, null=True, blank=True)
    source_release_date = models.DateField()
    cdm_release_date = models.DateField()
    cdm_version = models.CharField(max_length=10, null=True, blank=True)
    cdm_version_concept_id = models.ForeignKey(Concept, on_delete=DEFAULT_ON_DELETE)
    vocabulary_version = models.CharField(max_length=20)
