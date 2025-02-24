import client

mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")
collection= client.get_collection(db, "employees")

collection2 = client.get_collection(db, "inv_rec")

# Deleting all documents in the collection
# delete_result = collection2.delete_many({})


collection2.drop()
print("documents deleted.")
