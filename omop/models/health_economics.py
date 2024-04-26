from django.contrib import admin
from django.db import models
from omop.models import DEFAULT_ON_DELETE

from omop.models.clinical_data import Person
from omop.models.vocabularies import Concept, Domain


class Cost(models.Model):
    """CREATE TABLE @cdmDatabaseSchema.COST (
                        cost_id integer NOT NULL,
                        cost_event_id integer NOT NULL,
                        cost_domain_id varchar(20) NOT NULL,
                        cost_type_concept_id integer NOT NULL,
                        currency_concept_id integer NULL,
                        total_charge NUMERIC NULL,
                        total_cost NUMERIC NULL,
                        total_paid NUMERIC NULL,
                        paid_by_payer NUMERIC NULL,
                        paid_by_patient NUMERIC NULL,
                        paid_patient_copay NUMERIC NULL,
                        paid_patient_coinsurance NUMERIC NULL,
                        paid_patient_deductible NUMERIC NULL,
                        paid_by_primary NUMERIC NULL,
                        paid_ingredient_cost NUMERIC NULL,
                        paid_dispensing_fee NUMERIC NULL,
                        payer_plan_period_id integer NULL,
                        amount_allowed NUMERIC NULL,
                        revenue_code_concept_id integer NULL,
                        revenue_code_source_value varchar(50) NULL,
                        drg_concept_id integer NULL,
                        drg_source_value varchar(3) NULL );
    ALTER TABLE @cdmDatabaseSchema.COST ADD CONSTRAINT xpk_COST PRIMARY KEY (cost_id);
    """

    cost_id = models.IntegerField(primary_key=True)
    cost_event_id = models.IntegerField()
    cost_domain_id = models.ForeignKey(Domain, max_length=20, on_delete=DEFAULT_ON_DELETE)
    cost_type_concept = models.ForeignKey(
        Concept, on_delete=DEFAULT_ON_DELETE, related_name="cost_type_concept_ids"
    )
    currency_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="currency_concept_ids",
    )
    total_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_by_payer = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_by_patient = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_patient_copay = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    paid_patient_coinsurance = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    paid_patient_deductible = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    paid_by_primary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_ingredient_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    paid_dispensing_fee = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    payer_plan_period_id = models.IntegerField(null=True, blank=True)
    amount_allowed = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    revenue_code_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="revenue_code_concept_ids",
    )
    revenue_code_source_value = models.CharField(max_length=50, null=True, blank=True)
    drg_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="drg_concept_ids",
    )
    drg_source_value = models.CharField(max_length=3, null=True, blank=True)


class CostAdmin(admin.ModelAdmin):
    raw_id_fields = (
        "cost_domain_id",
        "cost_type_concept",
        "currency_concept",
        "revenue_code_concept",
        "drg_concept",
    )
    autocomplete_fields = (
        "cost_domain_id",
        "cost_type_concept",
        "currency_concept",
        "revenue_code_concept",
        "drg_concept",
    )
    search_fields = (
        "cost_domain_id__domain_id",
        "cost_type_concept__concept_name",
        "currency_concept__concept_name",
        "revenue_code_concept__concept_name",
        "drg_concept__concept_name",
    )


class PayerPlanPeriod(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.PAYER_PLAN_PERIOD (
                        payer_plan_period_id integer NOT NULL,
                        person_id integer NOT NULL,
                        payer_plan_period_start_date date NOT NULL,
                        payer_plan_period_end_date date NOT NULL,
                        payer_concept_id integer NULL,
                        payer_source_value varchar(50) NULL,
                        payer_source_concept_id integer NULL,
                        plan_concept_id integer NULL,
                        plan_source_value varchar(50) NULL,
                        plan_source_concept_id integer NULL,
                        sponsor_concept_id integer NULL,
                        sponsor_source_value varchar(50) NULL,
                        sponsor_source_concept_id integer NULL,
                        family_source_value varchar(50) NULL,
                        stop_reason_concept_id integer NULL,
                        stop_reason_source_value varchar(50) NULL,
                        stop_reason_source_concept_id integer NULL );
    ALTER TABLE @cdmDatabaseSchema.PAYER_PLAN_PERIOD
    ADD CONSTRAINT xpk_PAYER_PLAN_PERIOD PRIMARY KEY (payer_plan_period_id);
    """

    payer_plan_period_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=DEFAULT_ON_DELETE)
    payer_plan_period_start_date = models.DateField()
    payer_plan_period_end_date = models.DateField()
    payer_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="payer_concept_ids",
    )
    payer_source_value = models.CharField(max_length=50, null=True, blank=True)
    payer_source_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="payer_source_concept_ids",
    )
    plan_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="plan_concept_ids",
    )
    plan_source_value = models.CharField(max_length=50, null=True, blank=True)
    plan_source_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="plan_source_concept_ids",
    )
    sponsor_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="sponsor_concept_ids",
    )
    sponsor_source_value = models.CharField(max_length=50, null=True, blank=True)
    sponsor_source_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="sponsor_source_concept_ids",
    )
    family_source_value = models.CharField(max_length=50, null=True, blank=True)
    stop_reason_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="stop_reason_concept_ids",
    )
    stop_reason_source_value = models.CharField(max_length=50, null=True, blank=True)
    stop_reason_source_concept = models.ForeignKey(
        Concept,
        on_delete=DEFAULT_ON_DELETE,
        null=True,
        blank=True,
        related_name="stop_reason_source_concept_ids",
    )


class PayerPlanPeriodAdmin(admin.ModelAdmin):
    raw_id_fields = (
        "person",
        "payer_concept",
        "payer_source_concept",
        "plan_concept",
        "plan_source_concept",
        "sponsor_concept",
        "sponsor_source_concept",
        "stop_reason_concept",
        "stop_reason_source_concept",
    )
    autocomplete_fields = (
        "person",
        "payer_concept",
        "payer_source_concept",
        "plan_concept",
        "plan_source_concept",
        "sponsor_concept",
        "sponsor_source_concept",
        "stop_reason_concept",
        "stop_reason_source_concept",
    )
    search_fields = (
        "person__person_id",
        "payer_concept__concept_name",
        "payer_source_concept__concept_name",
        "plan_concept__concept_name",
        "plan_source_concept__concept_name",
        "sponsor_concept__concept_name",
        "sponsor_source_concept__concept_name",
        "stop_reason_concept__concept_name",
        "stop_reason_source_concept__concept_name",
    )
