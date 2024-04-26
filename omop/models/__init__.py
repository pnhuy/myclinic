from omop.models.constants import DEFAULT_ON_DELETE
from omop.models.clinical_data import (
    ConditionOccurrence,
    DeviceExposure,
    DrugExposure,
    Episode,
    EpisodeEvent,
    FactRelationship,
    Measurement,
    Note,
    NoteNlp,
    Observation,
    ObservationPeriod,
    Person,
    ProcedureOccurrence,
    Specimen,
    VisitDetail,
    VisitOccurrence,
)
from omop.models.derived_elements import Cohort, CohortDefinition, ConditionEra, DoseEra, DrugEra
from omop.models.health_economics import Cost, PayerPlanPeriod
from omop.models.health_system import CareSite, Location, Provider
from omop.models.metadata import CdmSource, Metadata
from omop.models.vocabularies import (
    Concept,
    ConceptAncestor,
    ConceptClass,
    ConceptRelationship,
    ConceptSynonym,
    Domain,
    DrugStrength,
    Relationship,
    SourceToConceptMap,
    Vocabulary,
)

OMOP_TABLES = [
    # Standardized clinical data
    Person,
    ObservationPeriod,
    VisitOccurrence,
    VisitDetail,
    ConditionOccurrence,
    DrugExposure,
    ProcedureOccurrence,
    DeviceExposure,
    Measurement,
    Observation,
    Note,
    NoteNlp,
    Episode,
    EpisodeEvent,
    Specimen,
    FactRelationship,
    # Standarized health system
    Location,
    CareSite,
    Provider,
    # Standardized health economics
    Cost,
    PayerPlanPeriod,
    # Standardized derived elements
    ConditionEra,
    DrugEra,
    DoseEra,
    Cohort,
    CohortDefinition,
    # Standardized metadata
    CdmSource,
    Metadata,
    # Standardized vocabularies
    Concept,
    Vocabulary,
    Domain,
    ConceptClass,
    ConceptSynonym,
    ConceptRelationship,
    Relationship,
    ConceptAncestor,
    SourceToConceptMap,
    DrugStrength,
]

__all__ = ["OMOP_TABLES", "DEFAULT_ON_DELETE"]
