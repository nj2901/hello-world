# Imports the Google Cloud client library
from google.cloud import bigquery
from DatasetExists import exists
# Instantiates a client
bqclient = bigquery.Client()

# The name for the dataset to check whether it exists or not
dataset_name = 'demo_dataset'
print(exists(dataset_name,bqclient))

