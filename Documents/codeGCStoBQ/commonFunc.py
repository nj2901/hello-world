def get_parameters(filename):
	f = open(filename)
	params = {}
	for line in f:
		line = line.strip()
		elements = line.split("=")
		key = elements[0].strip()
		value = elements[1].strip()
		params[key] = value
	f.close()
	return params


def get_columns():
	f = open("columns.txt")
	cols = []
	for line in f:
		line = line.strip()
		cols.append(line)
	f.close()
	return cols


def load_schema():
	f = open("schema.txt")
	schema = f.read().strip()
	return schema

# pass the name of dataset you want to check for existence and bigquery client object
def datasetExists(dataset_name,client):
	dataset_names_list = []
	for dataset in client.list_datasets():
		#print dataset
		d_name = dataset.dataset_id.encode('ascii','ignore')
		dataset_names_list.append(d_name)

	if dataset_name in dataset_names_list:
		return True
	else:
		return False

# pass the name of table you want to check for existence , dataset and bigquery client object
def tableExists(table_name,dataset,client):
	#dataset_names_list = []
	table_names_list = []
	for table in client.list_dataset_tables(dataset):
		t_name = table.table_id.encode('ascii','ignore')
		table_names_list.append(t_name)
	
	if table_name in table_names_list:
		return True
	else:
		return False
