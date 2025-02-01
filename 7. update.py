import client

if __name__ == "__main__":
    print("pymongo is running")
    mongo_client= client.get_mongo_client()
    db= client.get_database(mongo_client, "mydb1")
    collection= client.get_collection(db, "mycollection1")

    filter= {'_id': 124}
    update= {'$set': {'name': 'new_ne'} }

    updated= collection.update_one( filter, update)

    doc= collection.find()
    for d in doc:
        print(d)
    print(updated.modified_count)
    
