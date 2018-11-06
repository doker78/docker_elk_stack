...
 
# Set up a tag create spec.
tag_create_spec = tag_stub.CreateSpec(name=’red’,
                                      description=’My favorite color’,
                                      category_id=fav_category_id)
 
# Create the tag.
tag_stub = tagging_client.Tag(my_stub_config)
tag_id = tag_stub.create(create_spec)