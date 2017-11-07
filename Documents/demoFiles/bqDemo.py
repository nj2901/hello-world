# Imports the Google Cloud client library
from google.cloud import bigquery

# Instantiates a client
client = bigquery.Client(project = 'cp-100-demo-project')

dataset_name = 'my_new_dataset'
dataset_names_list = []
for dataset in client.list_datasets():
	#print dataset
	d_name = dataset.dataset_id.encode('ascii','ignore')
	dataset_names_list.append(d_name)

if dataset_name in dataset_names_list:
	print "dataset exists"
else:
	print "doesn't exists"
	
	

