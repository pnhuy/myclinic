from django.db import models


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
    """
    cost_id = models.IntegerField(primary_key=True)
    cost_event_id = models.IntegerField()
    cost_domain_id = models.CharField(max_length=20)
    cost_type_concept_id = models.IntegerField()
    currency_concept_id = models.IntegerField(null=True, blank=True)
    total_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_by_payer = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_by_patient = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_patient_copay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_patient_coinsurance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_patient_deductible = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_by_primary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_ingredient_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_dispensing_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payer_plan_period_id = models.IntegerField(null=True, blank=True)
    amount_allowed = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    revenue_code_concept_id = models.IntegerField(null=True, blank=True)
    revenue_code_source_value = models.CharField(max_length=50, null=True, blank=True)
    drg_concept_id = models.IntegerField(null=True, blank=True)
    drg_source_value = models.CharField(max_length=3, null=True, blank=True)

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
    """
    payer_plan_period_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    payer_plan_period_start_date = models.DateField()
    payer_plan_period_end_date = models.DateField()
    payer_concept_id = models.IntegerField(null=True, blank=True)
    payer_source_value = models.CharField(max_length=50, null=True, blank=True)
    payer_source_concept_id = models.IntegerField(null=True, blank=True)
    plan_concept_id = models.IntegerField(null=True, blank=True)
    plan_source_value = models.CharField(max_length=50, null=True, blank=True)
    plan_source_concept_id = models.IntegerField(null=True, blank=True)
    sponsor_concept_id = models.IntegerField(null=True, blank=True)
    sponsor_source_value = models.CharField(max_length=50, null=True, blank=True)
    sponsor_source_concept_id = models.IntegerField(null=True, blank=True)
    family_source_value = models.CharField(max_length=50, null=True, blank=True)
    stop_reason_concept_id = models.IntegerField(null=True, blank=True)
    stop_reason_source_value = models.CharField(max_length=50, null=True, blank=True)
    stop_reason_source_concept_id = models.IntegerField(null=True, blank=True)
