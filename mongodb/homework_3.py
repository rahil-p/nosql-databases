import pymongo

client = pymongo.MongoClient()
db = client.test_database
collection = db.movies

#a
collection.update_many({'rated':'NOT RATED'},
		       {'$set':{'rated':'Pending rating'}})

#b
collection.insert_one({'title':'Raising Arizona',
		       'year':'1987',
                       'countries':['USA'],
		       'genres':['Comedy','Crime'],
		       'directors':['Joel Coen','Ethan Coen'],
		       'imdb':{'id':93822,
			       'rating':7.4,
			       'votes':110554}})

#c		       
n_pipeline = [{'$group':{'_id':'Comedy','count':{'$sum':1}}}]
n = collection.aggregate(n_pipeline)
print(list(n))

#d
country_pipeline = [{'$group':{'_id':'USA + Pending rating','count':{'$sum':1}}}]
country = collection.aggregate(country_pipeline)
print(list(country))

#e
db.shop.insert([{'_id':1,'name':'milk','price':3}, 
		{'_id':2,'name':'chocolate','price':1}])
db.warehouse.insert([{'_id':1,'name_w':'butter','expired':0}, 
		     {'_id':2,'name_w':'chocolate','expired':0},
		     {'_id':3,'name_w':'milk','expired':1}])
ts_pipeline = [{'$lookup':{'from':'warehouse',
			   'localField':'name',
			   'foreignField':'name_w',
			   'as':'inventory_check'}}]
ts = db.shop.aggregate(ts_pipeline)
print(list(ts))



