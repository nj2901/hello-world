# pass the name of dataset you want to check for existence and bigquery client object
def exists(dataset_name,client):
	dataset_names_list = []
	for dataset in client.list_datasets():
		#print dataset
		d_name = dataset.dataset_id.encode('ascii','ignore')
		dataset_names_list.append(d_name)

	if dataset_name in dataset_names_list:
		return "exists"
	else:
		return "doesn't exists"

