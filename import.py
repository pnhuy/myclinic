import argparse
import os
from django.db import models
import pandas as pd
from tqdm.auto import tqdm
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myclinic.settings')
django.setup()


from omop.models import Concept, Domain, Vocabulary, ConceptClass



def cli():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', type=str)

    args = argparser.parse_args()

    return args

if __name__ == '__main__':
    args = cli()
    input_path = args.input
    if not input_path:
        raise ValueError('Input path is required')
    concept_csv = pd.read_csv(os.path.join(input_path, 'CONCEPT.csv'), sep='\t', keep_default_na=False, na_values=['']).replace({pd.NA: None})
    domain_csv = pd.read_csv(os.path.join(input_path, 'DOMAIN.csv'), sep='\t', keep_default_na=False, na_values=['']).replace({pd.NA: None})
    vocabulary_csv = pd.read_csv(os.path.join(input_path, 'VOCABULARY.csv'), sep='\t', keep_default_na=False, na_values=['']).replace({pd.NA: None})
    concept_class_csv = pd.read_csv(os.path.join(input_path, 'CONCEPT_CLASS.csv'), sep='\t', keep_default_na=False, na_values=['']).replace({pd.NA: None})

    # import domain
    for _, row in tqdm(domain_csv.iterrows(), total=len(domain_csv), desc='Importing domain'):
        Domain(**row).save()

    # import vocabulary
    for _, row in tqdm(vocabulary_csv.iterrows(), total=len(vocabulary_csv), desc='Importing vocabulary'):
        Vocabulary(**row).save()

    # import concept class
    for _, row in tqdm(concept_class_csv.iterrows(), total=len(concept_class_csv), desc='Importing concept class'):
        ConceptClass(**row).save()

    # import concept
    for _, row in tqdm(concept_csv.iterrows(), total=len(concept_csv), desc='Importing concept'):
        try:
            data = row.to_dict()
            data['concept_name'] = str(data['concept_name'])
            data['domain_id'] = Domain.objects.get(domain_id=str(data['domain_id']))
            data['vocabulary_id'] = Vocabulary.objects.get(vocabulary_id=str(data['vocabulary_id']))
            data['concept_class_id'] = ConceptClass.objects.get(concept_class_id=str(data['concept_class_id']))
            data['valid_start_date'] = str(data['valid_start_date'])
            data['valid_end_date'] = str(data['valid_end_date'])
            Concept(**data).save()
        except Exception as e:
            print(e)
            print(row.to_dict())
            import pdb; pdb.set_trace()

         
      

    
