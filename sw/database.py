import pymongo


class DB(object):
    DATABASE = None
    DSN = "mongodb://mongodb:27017"

    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.DSN)
        DB.DATABASE = client['sample_app']

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def all(collection):
        return DB.DATABASE[collection].find()

    @staticmethod
    def find(collection, query):
        return DB.DATABASE[collection].find(query)

    @staticmethod
    def update_one(collection: str, filter_query: dict, update: dict, upsert: bool = False):
        return DB.DATABASE[collection].update_one(filter_query, update, upsert)
