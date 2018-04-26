import pymongo

client = MongoClient()
database = client.store

collection = database.sales
collection.find({"items.fruit": "banana"}).count()
