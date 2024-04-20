from django.db import models


class Location(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.LOCATION (
			location_id integer NOT NULL,
			address_1 varchar(50) NULL,
			address_2 varchar(50) NULL,
			city varchar(50) NULL,
			state varchar(2) NULL,
			zip varchar(9) NULL,
			county varchar(20) NULL,
			location_source_value varchar(50) NULL,
			country_concept_id integer NULL,
			country_source_value varchar(80) NULL,
			latitude NUMERIC NULL,
			longitude NUMERIC NULL );
    ALTER TABLE @cdmDatabaseSchema.LOCATION ADD CONSTRAINT xpk_LOCATION PRIMARY KEY (location_id);
    """
    location_id = models.IntegerField(primary_key=True)
    address_1 = models.CharField(max_length=50, null=True, blank=True)
    address_2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip = models.CharField(max_length=9, null=True, blank=True)
    county = models.CharField(max_length=20, null=True, blank=True)
    location_source_value = models.CharField(max_length=50, null=True, blank=True)
    country_concept_id = models.IntegerField(null=True, blank=True)
    country_source_value = models.CharField(max_length=80, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)


class CareSite(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CARE_SITE (
			care_site_id integer NOT NULL,
			care_site_name varchar(255) NULL,
			place_of_service_concept_id integer NULL,
			location_id integer NULL,
			care_site_source_value varchar(50) NULL,
			place_of_service_source_value varchar(50) NULL );
    ALTER TABLE @cdmDatabaseSchema.CARE_SITE ADD CONSTRAINT xpk_CARE_SITE PRIMARY KEY (care_site_id);
    """
    care_site_id = models.IntegerField(primary_key=True)
    care_site_name = models.CharField(max_length=255, null=True, blank=True)
    place_of_service_concept_id = models.IntegerField(null=True, blank=True)
    location_id = models.IntegerField(null=True, blank=True)
    care_site_source_value = models.CharField(max_length=50, null=True, blank=True)
    place_of_service_source_value = models.CharField(max_length=50, null=True, blank=True)


class Provider(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.PROVIDER (
			provider_id integer NOT NULL,
			provider_name varchar(255) NULL,
			npi varchar(20) NULL,
			dea varchar(20) NULL,
			specialty_concept_id integer NULL,
			care_site_id integer NULL,
			year_of_birth integer NULL,
			gender_concept_id integer NULL,
			provider_source_value varchar(50) NULL,
			specialty_source_value varchar(50) NULL,
			specialty_source_concept_id integer NULL,
			gender_source_value varchar(50) NULL,
			gender_source_concept_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.PROVIDER ADD CONSTRAINT xpk_PROVIDER PRIMARY KEY (provider_id);
    """
    provider_id = models.IntegerField(primary_key=True)
    provider_name = models.CharField(max_length=255, null=True, blank=True)
    npi = models.CharField(max_length=20, null=True, blank=True)
    dea = models.CharField(max_length=20, null=True, blank=True)
    specialty_concept_id = models.IntegerField(null=True, blank=True)
    care_site_id = models.IntegerField(null=True, blank=True)
    year_of_birth = models.IntegerField(null=True, blank=True)
    gender_concept_id = models.IntegerField(null=True, blank=True)
    provider_source_value = models.CharField(max_length=50, null=True, blank=True)
    specialty_source_value = models.CharField(max_length=50, null=True, blank=True)
    specialty_source_concept_id = models.IntegerField(null=True, blank=True)
    gender_source_value = models.CharField(max_length=50, null=True, blank=True)
    gender_source_concept_id = models.IntegerField(null=True, blank=True)


