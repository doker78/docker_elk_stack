# list of automation endpoint on vcenter server instances
service_infos = lookup_service_infos(prod='com.vmware.cis',
                                             svc_type='cs.vapi', 
                                             proto='vapi.json.https.public', 
                                             ep_type='com.vmware.vapi.endpoint',
                                             node_id=my_mgmt_node_id)
my_vapi_url = service_infos[0].serviceEndpoints[0].url