import argparse
import os
from types import FunctionType
from django.db import models
import pandas as pd
import numpy as np
from tqdm.auto import tqdm
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myclinic.settings")
django.setup()


from omop.models import (  # noqa
    Concept,
    Domain,
    Vocabulary,
    ConceptClass,
    ConceptRelationship,
    ConceptSynonym,
    ConceptAncestor,
    DrugStrength,
    Relationship,
)


def insert(csv_path: str, model: models.Model, process_fn: FunctionType):
    df = pd.read_csv(csv_path, sep="\t", keep_default_na=False, na_values=[""])
    df = df.replace({np.nan: None})
    print(csv_path)
    print(df.head())
    # df = df.sample(frac=0.1)
    # import pdb; pdb.set_trace()
    items = []
    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Importing {model.__name__}"):
        row = process_fn(row.to_dict())
        items.append(model(**row))
    model.objects.bulk_create(items, batch_size=1000, ignore_conflicts=True)


def cli():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", type=str)

    args = argparser.parse_args()

    return args


def process_fn(row):
    if "valid_start_date" in row:
        row["valid_start_date"] = str(row["valid_start_date"])
    if "valid_end_date" in row:
        row["valid_end_date"] = str(row["valid_end_date"])
    return row


if __name__ == "__main__":
    args = cli()
    input_path = args.input
    if not input_path:
        raise ValueError("Input path is required")

    # concept ancestor
    insert(
        os.path.join(input_path, "CONCEPT_ANCESTOR.csv"),
        ConceptAncestor,
        lambda row: row,
    )

    # concept class
    insert(
        os.path.join(input_path, "CONCEPT_CLASS.csv"),
        ConceptClass,
        lambda row: row,
    )

    # concept relationship
    insert(
        os.path.join(input_path, "CONCEPT_RELATIONSHIP.csv"),
        ConceptRelationship,
        process_fn,
    )

    # concept synonym
    insert(
        os.path.join(input_path, "CONCEPT_SYNONYM.csv"),
        ConceptSynonym,
        process_fn,
    )

    # concept
    insert(os.path.join(input_path, "CONCEPT.csv"), Concept, process_fn)

    # domain
    insert(os.path.join(input_path, "DOMAIN.csv"), Domain, process_fn)

    # drug strength
    insert(
        os.path.join(input_path, "DRUG_STRENGTH.csv"),
        DrugStrength,
        process_fn,
    )

    # relationship
    insert(
        os.path.join(input_path, "RELATIONSHIP.csv"),
        Relationship,
        process_fn,
    )

    # vocabulary
    insert(
        os.path.join(input_path, "VOCABULARY.csv"),
        Vocabulary,
        process_fn,
    )
