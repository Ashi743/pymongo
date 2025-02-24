import client
mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")

collection4= client.get_collection(db, "agg_db")

agg_grp = collection4.aggregate( [{"$group": {"_id": "$user", "Total Subjects": {"$sum": 2} } } ] )    

tot_score= collection4.aggregate ( [ {"$group": 
                                      {"_id": "$user", 
                                       "Total Score": {"$sum": "$score"} } } ] )

for doc in tot_score:
    print(doc)
    print("----")