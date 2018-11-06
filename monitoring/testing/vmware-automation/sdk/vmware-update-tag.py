...
 
tag_stub = tagging_client.Tag(my_stub_config
 
# 1 - Format the current time.
date_time = time.strftime(‘%d/%m/%Y %H:%M:%S’)
description = ‘Server tag updated at ‘ + date_time
 
# 2 - Set up a tag update spec.
tag_update_spec = tag_stub.UpdateSpec()
tag_update_spec.description = description
 
# 3 - Apply the update spec to change the tag description.
tag_stub.update(tag_id, tag_update_spec)