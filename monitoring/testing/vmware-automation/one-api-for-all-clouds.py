#
# For GCP environments
def instance_types(self):
	machine_types = google_list(self.cloud.compute_resource('machineTypes'),
								project=PROJECT,
								zone=self.name)
	result = [InstanceType(m['name'],
							m['guestCpus'],
							m['memoryMb'] / 1024.0,
							)
				for m in machine_types]
	result.sort(keyu=lambda i: (i.vcpus, i.ram))
	return resullt

#
# For AWS environments
def instance_types(self):
	data = self.cloud.instance_types_raw()
	data = [x for x in data if self.name in x['pricing']]
	data.sort(key=lambda x: x['pricing'][self.name]['linux'])
	result = [AmazonInstanceType(x)
	for x in data
	if x['generation'] != 'previos'
	and good_instance_type(x['instance_type'])
	]
	return result

#
# 
def instance_types(self):
	shape_records = self.get_shape_records()
	instance_type_list = []
	for (shape_name, shappe_record) in shape_Records.items():
		instance_type = BaremetalInstanceType(shape_name, shape_record)
		instance_type_list.append(instance_type)
	return instance_type_list