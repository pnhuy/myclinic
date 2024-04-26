from django.contrib import admin
from django.db import models

from omop.models import DEFAULT_ON_DELETE
from omop.models.vocabularies import Concept


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
    ALTER TABLE @cdmDatabaseSchema.LOCATION
    ADD CONSTRAINT xpk_LOCATION PRIMARY KEY (location_id);
    """

    location_id = models.IntegerField(primary_key=True)
    address_1 = models.CharField(max_length=50, null=True, blank=True)
    address_2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip = models.CharField(max_length=9, null=True, blank=True)
    county = models.CharField(max_length=20, null=True, blank=True)
    location_source_value = models.CharField(max_length=50, null=True, blank=True)
    country_concept = models.ForeignKey(
        Concept, on_delete=DEFAULT_ON_DELETE, null=True, blank=True
    )
    country_source_value = models.CharField(max_length=80, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return (f"[{self.location_id}] {self.address_1} {self.address_2} "
                f"{self.city} {self.state} {self.zip} {self.county} "
                f"{self.country_concept.concept_name}")


class LocationAdmin(admin.ModelAdmin):
    raw_id_fields = ("country_concept",)
    autocomplete_fields = ("country_concept",)
    search_fields = [
        "location_id",
        "address_1",
        "address_2",
        "city",
        "state",
        "zip",
        "county",
        "location_source_value",
        "country_source_value",
        "country_concept",
    ]


class CareSite(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CARE_SITE (
                        care_site_id integer NOT NULL,
                        care_site_name varchar(255) NULL,
                        place_of_service_concept_id integer NULL,
                        location_id integer NULL,
                        care_site_source_value varchar(50) NULL,
                        place_of_service_source_value varchar(50) NULL );
    ALTER TABLE @cdmDatabaseSchema.CARE_SITE
    ADD CONSTRAINT xpk_CARE_SITE PRIMARY KEY (care_site_id);
    """

    care_site_id = models.IntegerField(primary_key=True)
    care_site_name = models.CharField(max_length=255, null=True, blank=True)
    place_of_service_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="place_of_service_concept_ids",
    )
    location = models.ForeignKey(Location, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    care_site_source_value = models.CharField(max_length=50, null=True, blank=True)
    place_of_service_source_value = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"[{self.care_site_id}] {self.care_site_name} - {self.location.__str__()}"


class CareSiteAdmin(admin.ModelAdmin):
    raw_id_fields = ["place_of_service_concept", "location"]
    autocomplete_fields = ["place_of_service_concept", "location"]
    search_fields = [
        "care_site_id",
        "care_site_name",
        "care_site_source_value",
        "place_of_service_source_value",
    ]


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
    specialty_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="specialty_concept_ids",
    )
    care_site = models.ForeignKey(CareSite, on_delete=DEFAULT_ON_DELETE, null=True, blank=True)
    year_of_birth = models.IntegerField(null=True, blank=True)
    gender_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="gender_concept_ids",
    )
    provider_source_value = models.CharField(max_length=50, null=True, blank=True)
    specialty_source_value = models.CharField(max_length=50, null=True, blank=True)
    specialty_source_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="specialty_source_concept_ids",
    )
    gender_source_value = models.CharField(max_length=50, null=True, blank=True)
    gender_source_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="gender_source_concept_ids",
    )

    def __str__(self):
        return f"[{self.provider_id}] {self.provider_name}"


class ProviderAdmin(admin.ModelAdmin):
    raw_id_fields = (
        "specialty_concept",
        "care_site",
        "gender_concept",
        "specialty_source_concept",
        "gender_source_concept",
    )
    autocomplete_fields = (
        "specialty_concept",
        "care_site",
        "gender_concept",
        "specialty_source_concept",
        "gender_source_concept",
    )
    search_fields = ("__str__",)
