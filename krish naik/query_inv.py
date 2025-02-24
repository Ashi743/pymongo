import client

mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")
collection1 = client.get_collection(db, "inventory")

docs= collection1.find()

print('&&&&&&&&'*10)
for doc in docs:
    print(doc)
    print("----")

#querying nested
print('&&&&&&&&'*10)
for record in collection1.find( {"size": {"h": 14, "w": 21, "uom": "cm"}}):
    print('-----------'*10)
    print(record)
    print('-----------'*10)