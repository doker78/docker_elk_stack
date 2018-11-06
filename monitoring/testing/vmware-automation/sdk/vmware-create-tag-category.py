...
 
category_stub = tagging_client.Category(my_stub_config)
 
# Set up a tag category create spec.
tc_create_spec = category_stub.CreateSpec(name = ‘favorites’,
                                          description = ‘My favorite virtual machines’,
                                          cardinality = CategoryModel.Cardinality.MULTIPLE,
                                          associable_types = set())
 
# Create the tag category.
fav_category_id = category_stub.create(create_spec)