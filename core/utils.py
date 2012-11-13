def update_entity_properties(entity, data):
    """ Updates given entity properties according to the keys/values in the
    dict and returns the entity. Note that this does not save the entity """
    for key in data:
        setattr(entity, key, data[key])
    return entity


def get_entity_properties(entity):
    """ Returns dict will entity properties and their values """
    return dict([(key, getattr(entity, key)) for key in entity.properties()])