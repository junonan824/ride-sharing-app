from bson import json_util, ObjectId

def json_response(data):
    return json_util.dumps(data)

def serialize_doc(doc):
    """Convert MongoDB document to a JSON-serializable format."""
    doc['_id'] = str(doc['_id'])
    return doc