import client

mongo_client = client.get_mongo_client()

# Access the database and collection
db = client.get_database(mongo_client, "mydb22")
collection1 = client.get_collection(db, "mycollection22")
collection2 = client.get_collection(db, "mycollection23")

documents= [
    {"_id": 1, "name": "John", "age": 28},
    {"_id": 2, "name": "Jane", "age": 26},
    {"_id": 3, "name": "Tom", "age": 32},
    {"_id": 4, "name": "Anne", "age": 29}
]

collection1.insert_many(documents)
collection2.insert_many(documents)