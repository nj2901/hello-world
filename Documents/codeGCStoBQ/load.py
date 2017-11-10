from google.cloud import bigquery
from google.cloud import storage
import commonFunc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Enter the CSV file name")
parser.add_argument("tablename", help="Enter the destination table name")
args = parser.parse_args()

if args.filename.endswith(".csv"):
	#print args.filename
	FILE_NAME = args.filename
	TABLE_NAME = args.tablename
	params = commonFunc.get_parameters("constantParameters.txt")
	columns = commonFunc.get_columns()
	schema = commonFunc.load_schema()
	PROJECT_ID = params.get("PROJECT_ID",None)
	print PROJECT_ID
	DATASET_ID = params.get("DATASET_ID",None)
	print DATASET_ID
	BUCKET_NAME = params.get("BUCKET_NAME",None)
	print BUCKET_NAME
	storage_client = storage.Client(project=PROJECT_ID)
	bigquery_client = bigquery.Client(project=PROJECT_ID)
	bucket = storage.bucket.Bucket(storage_client,BUCKET_NAME)
	print bucket.exists()
	print commonFunc.datasetExists(DATASET_ID,bigquery_client)
	dataset_ref = bigquery_client.dataset(DATASET_ID)
	dataset = bigquery.Dataset(dataset_ref)
	#print commonFunc.tableExists(TABLE_NAME,dataset,bigquery_client)
	if bucket.exists() :
		GS_URL = 'gs://{}/{}'.format(BUCKET_NAME, FILE_NAME)
		table_ref = dataset.table(TABLE_NAME)
		table = bigquery.Table(table_ref)
		table.schema = [
			bigquery.SchemaField('NAME', 'STRING', mode='required'),
		 	bigquery.SchemaField('SNO', 'INTEGER', mode='required'),
		 	bigquery.SchemaField('COUNTRY', 'STRING', mode='required'),
		 	bigquery.SchemaField('AGE', 'INTEGER', mode='required'),
		 	bigquery.SchemaField('CITY', 'STRING', mode='required'),
		]
		if not commonFunc.tableExists(TABLE_NAME,dataset,bigquery_client) :
			bigquery_client.create_table(table)
		job_id_prefix = "my_load_job"
		job_config = bigquery.LoadJobConfig()
		job_config.create_disposition = 'NEVER'
    		job_config.skip_leading_rows = 1
    		job_config.source_format = 'CSV'
    		job_config.write_disposition = 'WRITE_APPEND'
    		load_job = bigquery_client.load_table_from_uri(
        		GS_URL, table_ref, job_config=job_config,
        		job_id_prefix=job_id_prefix)
        	print "\n\nJOB " + load_job.state
		if load_job.state == 'RUNNING' :
			if load_job.job_type == 'load' :
				load_job.result()
	else:
		print "bucket you specified doesn't exists"
	
else :
	print "Enter a CSV file."
