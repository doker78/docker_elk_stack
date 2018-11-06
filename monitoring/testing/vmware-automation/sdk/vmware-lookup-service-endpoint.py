def to lookup_single_service_info(prod, svc_type, proto, ep_type, node_id) :

   # 1 - Create a filter criterion for service info.
   filter_service_type = \
my_ls_stub.factory.create('ns0:LookupServiceRegistrationServiceType')
   filter_service_type.product = prod
   filter_service_type.type = svc_type

   # 2 - Create a filter criterion for endpoint info.
   filter_endpoint_type = \
my_ls_stub.factory.create('ns0:LookupServiceRegistrationEndpointType')
   filter_endpoint_type.protocol = proto
   filter_endpoint_type.type = ep_type

   # 3 - Create the registration filter object.
   filter_criteria = \
my_ls_stub.factory.create('ns0:LookupServiceRegistrationFilter')
   filter_criteria.serviceType = filter_service_type
   filter_criteria.endpointType = filter_endpoint_type
   filter_criteria.nodeId = node_id

   # 4 - Retrieve specified service info with the List() method.
   service_infos = my_ls_stub.service.List(service_registration,
filter_criteria)
   return service_infos