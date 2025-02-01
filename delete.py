import client

mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")
collection= client.get_collection(db, "mycollection1")

collection.delete_one({'_id': 126})

doc= collection.find()
for d in doc:
    print(d)