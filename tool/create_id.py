from bson.objectid import ObjectId

def create_id():
    return str(ObjectId())