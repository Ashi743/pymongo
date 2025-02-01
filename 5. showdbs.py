import client
mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")
collection= client.get_collection(db, "mycollection1")

all_dbs= mongo_client.list_database_names()
print(all_dbs)

all_collections= db.list_collection_names()
print(all_collections)

all_docs= collection.find().limit(1)
print(collection.count_documents({}))

print(len(list(all_docs)))
print(all_docs)