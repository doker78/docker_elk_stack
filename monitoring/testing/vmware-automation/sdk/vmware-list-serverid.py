# list of vcenter ids by using lookup service
def get_mgmt_node_id(node_instance_name) :

   # 1 - List the vCenter Server instances.
   mgmt_node_infos = lookup_service_infos(prod='com.vmware.cis',
                                          svc_type='vcenterserver',
                                          proto='vmomi', ep_type='com.vmware.vim',
                                          node_id='*')

   # 2 - Find the matching node name and save the ID.
   for node in mgmt_node_infos :
     for attribute in node.serviceAttributes :
       if attribute.key == 'com.vmware.vim.vcenter.instanceName' :
         if attribute.value == node_instance_name :
           return node.nodeId