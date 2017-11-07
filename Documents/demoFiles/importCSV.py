##file to load csv file from local machine to bigquery table

import csv

from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField

client = bigquery.Client()

SCHEMA = [
    SchemaField('sno', 'INTEGER', mode='required'),
    SchemaField('full_name', 'STRING', mode='required'),
    SchemaField('age', 'INTEGER', mode='required'),
]

dataset_name = 'my_new_dataset'

table_ref = client.dataset(dataset_name).table('table_name')

load_config = LoadJobConfig()
load_config.skip_leading_rows = 1
load_config.schema = SCHEMA

# Contents of csv_file.csv:
#     Name,Age
#     Tim,99
with open('csv_file.csv', 'rb') as readable:
    client.load_table_from_file(
        readable, table_ref, job_config=load_config)  # API request
