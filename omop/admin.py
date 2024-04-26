from django.contrib import admin
from omop.models.clinical_data import (
    ConditionOccurrence,
    ConditionOccurrenceAdmin,
    Death,
    DeathAdmin,
    DeviceExposure,
    DeviceExposureAdmin,
    DrugExposure,
    DrugExposureAdmin,
    Episode,
    EpisodeAdmin,
    EpisodeEvent,
    EpisodeEventAdmin,
    FactRelationship,
    FactRelationshipAdmin,
    Measurement,
    MeasurementAdmin,
    Note,
    NoteAdmin,
    NoteNlp,
    NoteNlpAdmin,
    Observation,
    ObservationAdmin,
    ObservationPeriod,
    ObservationPeriodAdmin,
    Person,
    PersonAdmin,
    ProcedureOccurrence,
    ProcedureOccurrenceAdmin,
    Specimen,
    SpecimenAdmin,
    VisitDetail,
    VisitDetailAdmin,
    VisitOccurrence,
    VisitOccurrenceAdmin,
)
from omop.models.derived_elements import (
    Cohort,
    CohortDefinition,
    CohortDefinitionAdmin,
    ConditionEra,
    ConditionEraAdmin,
    DoseEra,
    DoseEraAdmin,
    DrugEra,
    DrugEraAdmin,
)
from omop.models.health_economics import Cost, CostAdmin, PayerPlanPeriod, PayerPlanPeriodAdmin
from omop.models.health_system import (
    CareSite,
    CareSiteAdmin,
    Location,
    LocationAdmin,
    Provider,
    ProviderAdmin,
)
from omop.models.metadata import CdmSource, Metadata
from omop.models.vocabularies import (
    Concept,
    ConceptAdmin,
    ConceptAncestor,
    ConceptAncestorAdmin,
    ConceptClass,
    ConceptClassAdmin,
    ConceptRelationship,
    ConceptRelationshipAdmin,
    ConceptSynonym,
    ConceptSynonymAdmin,
    Domain,
    DomainAdmin,
    DrugStrength,
    DrugStrengthAdmin,
    Relationship,
    RelationshipAdmin,
    SourceToConceptMap,
    SourceToConceptMapAdmin,
    Vocabulary,
    VocabularyAdmin,
)

# clinical_data
admin.site.register(Person, PersonAdmin)
admin.site.register(ObservationPeriod, ObservationPeriodAdmin)
admin.site.register(Death, DeathAdmin)
admin.site.register(VisitOccurrence, VisitOccurrenceAdmin)
admin.site.register(VisitDetail, VisitDetailAdmin)
admin.site.register(ConditionOccurrence, ConditionOccurrenceAdmin)
admin.site.register(DrugExposure, DrugExposureAdmin)
admin.site.register(ProcedureOccurrence, ProcedureOccurrenceAdmin)
admin.site.register(DeviceExposure, DeviceExposureAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(NoteNlp, NoteNlpAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(EpisodeEvent, EpisodeEventAdmin)
admin.site.register(Specimen, SpecimenAdmin)
admin.site.register(FactRelationship, FactRelationshipAdmin)

# derived elements
admin.site.register(ConditionEra, ConditionEraAdmin)
admin.site.register(DrugEra, DrugEraAdmin)
admin.site.register(DoseEra, DoseEraAdmin)
admin.site.register(Cohort)
admin.site.register(CohortDefinition, CohortDefinitionAdmin)

# health_economics
admin.site.register(Cost, CostAdmin)
admin.site.register(PayerPlanPeriod, PayerPlanPeriodAdmin)

# health_system
admin.site.register(CareSite, CareSiteAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Provider, ProviderAdmin)

# metadata
admin.site.register(Metadata)
admin.site.register(CdmSource)

# vocabularies
admin.site.register(Concept, ConceptAdmin)
admin.site.register(Vocabulary, VocabularyAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(ConceptClass, ConceptClassAdmin)
admin.site.register(ConceptRelationship, ConceptRelationshipAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(ConceptSynonym, ConceptSynonymAdmin)
admin.site.register(ConceptAncestor, ConceptAncestorAdmin)
admin.site.register(SourceToConceptMap, SourceToConceptMapAdmin)
admin.site.register(DrugStrength, DrugStrengthAdmin)
