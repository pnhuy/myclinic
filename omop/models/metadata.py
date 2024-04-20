from django.db import models

class Metadata(models.Model):
    metadata_id = models.IntegerField(primary_key=True)
    metadata_concept_id = models.IntegerField()
    metadata_type_concept_id = models.IntegerField()
    name = models.CharField(max_length=250)
    value_as_string = models.CharField(max_length=250, null=True, blank=True)
    value_as_concept_id = models.IntegerField(null=True, blank=True)
    value_as_number = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    metadata_date = models.DateField(null=True, blank=True)
    metadata_datetime = models.DateTimeField(null=True, blank=True)


class CdmSource(models.Model):
    cdm_source_name = models.CharField(max_length=255)
    cdm_source_abbreviation = models.CharField(max_length=25)
    cdm_holder = models.CharField(max_length=255)
    source_description = models.TextField(null=True, blank=True)
    source_documentation_reference = models.CharField(max_length=255, null=True, blank=True)
    cdm_etl_reference = models.CharField(max_length=255, null=True, blank=True)
    source_release_date = models.DateField()
    cdm_release_date = models.DateField()
    cdm_version = models.CharField(max_length=10, null=True, blank=True)
    cdm_version_concept_id = models.IntegerField()
    vocabulary_version = models.CharField(max_length=20)
