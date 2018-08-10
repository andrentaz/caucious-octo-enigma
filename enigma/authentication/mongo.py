import pymongo

def setup_connection(mongo_uri=None):
    global db
    db = _get_db_client(mongo_uri)


def _get_db_client(mongo_uri):
    db_name = mongo_uri.split("/")[-1]
    return pymongo.MongoClient(mongo_uri)[db_name]
