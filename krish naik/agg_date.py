import client
mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")

collection_date= client.get_collection(db, "date_db")
docs= collection_date.find()

agg_grp= collection_date.aggregate(
    [
        {"$group": 
        {"_id": "$item", 
        "avgAmount": {"$avg": {"$multiply": ["$price", "$quantity"]}},
        "avgqty": {"$avg": "$quantity"} 
        } 
        } 
    ] 
)

for doc in agg_grp:
    print(doc)


# as a select statement 

for row in collection_date.aggregate( [ { "$project": 
                                         { "day": { "$dayOfYear": "$date" }, 
                                          "year": { "$year": "$date" } } } ] ):
    print(row)