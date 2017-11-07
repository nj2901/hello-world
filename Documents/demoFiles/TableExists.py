# pass the name of dataset you want to check for existence and bigquery client object
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
