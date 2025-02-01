import client

# Get the MongoDB client from client.py
mongo_client = client.get_mongo_client()

# Access the database and collection
db = client.get_database(mongo_client, "mydb1")
collection = client.get_collection(db, "mycollection1")

# Insert documents into the collection
insert_dict = [
    {"_id": 1221, "name": "john", "marks": 50},
    {"_id": 124, "name": "jane", "marks": 60},
    {"_id": 125, "name": "jill", "marks": 70},
    {"_id": 126, "name": "joe", "marks": 80}
]
collection.insert_many(insert_dict)

print("Documents inserted successfully.")