from django.db import models


class Concept(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CONCEPT (
        concept_id integer NOT NULL,
        concept_name varchar(255) NOT NULL,
        domain_id varchar(20) NOT NULL,
        vocabulary_id varchar(20) NOT NULL,
        concept_class_id varchar(20) NOT NULL,
        standard_concept varchar(1) NULL,
        concept_code varchar(50) NOT NULL,
        valid_start_date date NOT NULL,
        valid_end_date date NOT NULL,
        invalid_reason varchar(1) NULL );
    ALTER TABLE @cdmDatabaseSchema.CONCEPT ADD CONSTRAINT xpk_CONCEPT PRIMARY KEY (concept_id);
    """
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=255)
    domain_id = models.CharField(max_length=20)
    vocabulary_id = models.CharField(max_length=20)
    concept_class_id = models.CharField(max_length=20)
    standard_concept = models.CharField(max_length=1, null=True, blank=True)
    concept_code = models.CharField(max_length=50)
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    invalid_reason = models.CharField(max_length=1, null=True, blank=True)


class Vocabulary(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.VOCABULARY (
			vocabulary_id varchar(20) NOT NULL,
			vocabulary_name varchar(255) NOT NULL,
			vocabulary_reference varchar(255) NULL,
			vocabulary_version varchar(255) NULL,
			vocabulary_concept_id integer NOT NULL );
    ALTER TABLE @cdmDatabaseSchema.VOCABULARY ADD CONSTRAINT xpk_VOCABULARY PRIMARY KEY (vocabulary_id);
    """
    vocabulary_id = models.CharField(max_length=20, primary_key=True)
    vocabulary_name = models.CharField(max_length=255)
    vocabulary_reference = models.CharField(max_length=255, null=True, blank=True)
    vocabulary_version = models.CharField(max_length=255, null=True, blank=True)
    vocabulary_concept_id = models.IntegerField()


class Domain(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.DOMAIN (
			domain_id varchar(20) NOT NULL,
			domain_name varchar(255) NOT NULL,
			domain_concept_id integer NOT NULL );
    ALTER TABLE @cdmDatabaseSchema.DOMAIN ADD CONSTRAINT xpk_DOMAIN PRIMARY KEY (domain_id);
    """
    domain_id = models.CharField(max_length=20, primary_key=True)
    domain_name = models.CharField(max_length=255)
    domain_concept_id = models.IntegerField()

class ConceptClass(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CONCEPT_CLASS (
			concept_class_id varchar(20) NOT NULL,
			concept_class_name varchar(255) NOT NULL,
			concept_class_concept_id integer NOT NULL );
    ALTER TABLE @cdmDatabaseSchema.CONCEPT_CLASS ADD CONSTRAINT xpk_CONCEPT_CLASS PRIMARY KEY (concept_class_id);
    """
    concept_class_id = models.CharField(max_length=20, primary_key=True)
    concept_class_name = models.CharField(max_length=255)
    concept_class_concept_id = models.IntegerField()

class ConceptRelationship(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CONCEPT_RELATIONSHIP (
			concept_id_1 integer NOT NULL,
			concept_id_2 integer NOT NULL,
			relationship_id varchar(20) NOT NULL,
			valid_start_date date NOT NULL,
			valid_end_date date NOT NULL,
			invalid_reason varchar(1) NULL );
    """
    concept_id_1 = models.IntegerField()
    concept_id_2 = models.IntegerField()
    relationship_id = models.CharField(max_length=20)
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    invalid_reason = models.CharField(max_length=1, null=True, blank=True)


class Relationship(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.RELATIONSHIP (
			relationship_id varchar(20) NOT NULL,
			relationship_name varchar(255) NOT NULL,
			is_hierarchical varchar(1) NOT NULL,
			defines_ancestry varchar(1) NOT NULL,
			reverse_relationship_id varchar(20) NOT NULL,
			relationship_concept_id integer NOT NULL );
    ALTER TABLE @cdmDatabaseSchema.RELATIONSHIP ADD CONSTRAINT xpk_RELATIONSHIP PRIMARY KEY (relationship_id);
    """
    relationship_id = models.CharField(max_length=20, primary_key=True)
    relationship_name = models.CharField(max_length=255)
    is_hierarchical = models.CharField(max_length=1)
    defines_ancestry = models.CharField(max_length=1)
    reverse_relationship_id = models.CharField(max_length=20)
    relationship_concept_id = models.IntegerField()


class ConceptSynonym(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CONCEPT_SYNONYM (
			concept_id integer NOT NULL,
			concept_synonym_name varchar(1000) NOT NULL,
			language_concept_id integer NOT NULL );
    """
    concept_id = models.IntegerField()
    concept_synonym_name = models.CharField(max_length=1000)
    language_concept_id = models.IntegerField()


class ConceptAncestor(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.CONCEPT_ANCESTOR (
			ancestor_concept_id integer NOT NULL,
			descendant_concept_id integer NOT NULL,
			min_levels_of_separation integer NOT NULL,
			max_levels_of_separation integer NOT NULL );
    """
    ancestor_concept_id = models.IntegerField()
    descendant_concept_id = models.IntegerField()
    min_levels_of_separation = models.IntegerField()
    max_levels_of_separation = models.IntegerField()


class SourceToConceptMap(models.Model):
    """
    CREATE TABLE @cdmDatabaseSchema.SOURCE_TO_CONCEPT_MAP (
			source_code varchar(50) NOT NULL,
			source_concept_id integer NOT NULL,
			source_vocabulary_id varchar(20) NOT NULL,
			source_code_description varchar(255) NULL,
			target_concept_id integer NOT NULL,
			target_vocabulary_id varchar(20) NOT NULL,
			valid_start_date date NOT NULL,
			valid_end_date date NOT NULL,
			invalid_reason varchar(1) NULL );
    """
    source_code = models.CharField(max_length=50)
    source_concept_id = models.IntegerField()
    source_vocabulary_id = models.CharField(max_length=20)
    source_code_description = models.CharField(max_length=255, null=True, blank=True)
    target_concept_id = models.IntegerField()
    target_vocabulary_id = models.CharField(max_length=20)
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    invalid_reason = models.CharField(max_length=1, null=True, blank=True)
