import pymongo
from pymongo import MongoClient


def get_mongo_client():
    return pymongo.MongoClient('mongodb://localhost:27017/')

def get_database(client, db_name):
    return client[db_name]

def get_collection(db, collection_name):
    return db[collection_name]

if __name__ ==  "__main__":
    print('pymongo is running')
    client= get_mongo_client()
    print(client)
