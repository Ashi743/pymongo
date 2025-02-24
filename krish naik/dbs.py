import client
mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")
collection= client.get_collection(db, "employees")

collection2 = client.get_collection(db, "inv_rec")

collection3= client.get_collection(db, "inv_update")

collection4= client.get_collection(db, "agg_db")

collection5= client.get_collection(db, "date_db")
docs= collection5.find()
for doc in docs:
    print(doc)
    print("----")