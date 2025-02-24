import client
mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")
collection= client.get_collection(db, "employees")

print('&&&&&&&&'*10)
for record in collection.find({'firstname': 'ashish'}):
    print('-----------'*10)
    print(record)
    print('-----------'*10)
print('&&&&&&&&'*10)


#using query operators   {$lte, $lt, $gt, $gte}
for record in collection.find( {'age': {'$gt': 30}}):
    print('-----------'*10)
    print(record)
    print('-----------'*10)
print('&&&&&&&&'*10)


#using query operators  {$in[], $nin}
for record in collection.find( {"department": {"$in": ["analytics"]}}):
    print('-----------'*10)
    print(record)
    print('-----------'*10)
print('&&&&&&&&'*10)

#using & operator
for record in collection.find( {"department": "analytics", "age": {"$gt": 30}}):
    print('-----------'*10)
    print(record)
    print('-----------'*10)

# using or operator
for record in collection.find( {"$and": [{"department": "analytics"}, {"age": {"$gt": 30}}]}):
    print('-----------'*10)
    print(record)
    print('-----------'*10)

print('&&&&&&&&'*10)

