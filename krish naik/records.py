import client

mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")

#collection= client.get_collection(db, "employees")
records= [
    {"_id":101, "firstname": "ashish", "lastname": "dangwal" ,"department": "analytics", "age": 30},
    {"_id":102, "firstname": "jane"  , "lastname": "doe"     ,"department": "analytics", "age": 25},
    {"_id":103, "firstname": "john"  , "lastname": "doe"     ,"department": "analytics", "age": 35},
    {"_id":104, "firstname": "jill"  , "lastname": "doe"     ,"department": "analytics", "age": 40}
]
#collection.insert_many(records)

#collection1= client.get_collection(db, "inventory")
inventory_records= [
    {"_id": 1, "item": "journal",   "qty": 25,  "size": {"h": 14,   "w": 21,    "uom": "cm"}, "status": "A"},
    {"_id": 2, "item": "notebook",  "qty": 50,  "size": {"h": 8.5,  "w": 11,    "uom": "in"}, "status": "A"},
    {"_id": 3, "item": "paper",     "qty": 100, "size": {"h": 8.5,  "w": 11,    "uom": "in"}, "status": "D"},
    {"_id": 4, "item": "planner",   "qty": 75,  "size": {"h": 22.85,"w": 30,    "uom": "cm"}, "status": "D"},
    {"_id": 5, "item": "postcard",  "qty": 45,  "size": {"h": 10,   "w": 15.25, "uom": "cm"}, "status": "A"}
]

#collection1.insert_many(inventory_records)

#collection3= client.get_collection(db, "inv_update")
inv_rec= [
     {"item": "canvas",
     "qty": 100,
     "size": {"h": 28, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "mat",
     "qty": 85,
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "mousepad",
     "qty": 25,
     "size": {"h": 19, "w": 22.85, "uom": "cm"},
     "status": "P"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "P"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 80,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "sketch pad",
     "qty": 95,
     "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
     "status": "A"}
]

#collection3.insert_many(inv_rec)

collection4 = client.get_collection(db, "agg_db")
agg_rec= [
     
    {"user":"Krish", "subject":"Database", "score":80}, 
    {"user":"Amit",  "subject":"JavaScript", "score":90}, 
    {"user":"Amit",  "title":"Database", "score":85}, 
    {"user":"Krish",  "title":"JavaScript", "score":75}, 
    {"user":"Amit",  "title":"Data Science", "score":60},
    {"user":"Krish",  "title":"Data Science", "score":95}
]

#collection4.insert_many(agg_rec)

#DATETIME
import datetime

#collection_date = client.get_collection(db, "date_db")
datetime_rec= [
{"_id": 1, 'item': "abc", "price": 10, "quantity": 2, "date": datetime.datetime(2020, 1, 1, 0, 0)},
{"_id": 2, 'item': "jkl", "price": 20, "quantity": 1, "date": datetime.datetime(2020, 2, 1, 0, 0)},
{"_id": 3, 'item': "xyz", "price": 5, "quantity": 5, "date": datetime.datetime(2020, 2, 1, 0, 0)},
{"_id": 4, 'item': "abc", "price": 10, "quantity": 10, "date": datetime.datetime(2020, 2, 15, 0, 0)},
 ]

#collection_date.insert_many(datetime_rec)
print("Documents inserted successfully.")

print(collection4.count_documents({}))