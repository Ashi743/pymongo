import client

mongo_client= client.get_mongo_client()
db= client.get_database(mongo_client, "mydb1")
collection3= client.get_collection(db, "inv_update")

#collection3.update_one( {"item": "journal"}, 
   #                    {"$set": {"size.uom":  "m" ,"status": "P"}, "$currentDate": {"lastModified": True} }  )

#collection3.update_many( {"qty": {"$lte" : 30}},
 #                       {"$set": {"size.w": 100, "status": "abhi change kiyela hai"}, "$currentDate": {"lastModified": True} } ),

collection3.replace_one( {"item": "canvas"}, {"item": "lolipop", "qty": 111, "size": { "w": 35.5, "uom": "cm"}, "status": "naya hai", 
                                              "instock": [
                                                {"warehouse": "A" , "qty": 60},
                                                {"warehouse": "B" , "qty": 420}
                                                ]  } )
print("document updated.")
