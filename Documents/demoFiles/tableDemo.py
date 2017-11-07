# Imports the Google Cloud client library
from google.cloud import bigquery
from DatasetExists import exists
from TableExists import tableExists
# Instantiates a client
client = bigquery.Client()

# The name for the dataset to check whether it exists or not
dataset_name = 'my_new_dataset'

## dataset reference in which we are looking for tables
dataset_ref = client.dataset(dataset_name)
dataset = bigquery.Dataset(dataset_ref)
dataset.description = 'my dataset whose tables are searched'

tables = list(client.list_dataset_tables(dataset))  # API request(s)
for table in tables:
	print table.table_id
	
#table name which is required to be searched
table_name = 'tableExistsDemo'
table_ref = dataset.table(table_name)
table = bigquery.Table(table_ref)

if tableExists(table_name,dataset,client):
	print "exists"
else:
	print "doesn't exists hence creating new table"
	client.create_table(table)                          # API request
tables = list(client.list_dataset_tables(dataset))  # API request(s)
for table in tables:
	print table.table_id

