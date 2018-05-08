# Put the use case you chose here. Then justify your database choice:
# -For a Hackernews use case, I selected MongoDB database because of its flexible design which allows
#  for creating a nesting hierarchy of sub-documents (e.g. sub-comments) in sub-documents (e.g.
#  comments) in documents (e.g. posts).
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# -MongoDB uses replication to create redundancies for failover. If the affected server is a primary
#  node, then a secondary server will be elected to replace it as the master.
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# -Data containing article information (content, score, comments) and user information (e.g. favorites,
#  login credentials, email) can be costly.  To mitigate the risk of lost data, article and user
#  information can be replicated into backups.  These processes can be automated to ensure recovery
#  in the case of lost data.

import pymongo

client = pymongo.MongoClient()
db = client.database
articles = db.articles
users = db.users

articles.insert([{'_id':1,
	       	  	  'title':"Java's Mysterious Interrupt",
				  'link':'https://carlmastrangelo.com/blog/javas-mysterious-interrupt',
				  'score_a':105,
				  'op':'clarkkent',
				  'comments':[]},

				 {'_id':2,
			       	  'title':'Thermal Paper Polaroid',
				  'link':'https://mitxela.com/projects/thermal_paper_polaroid',
				  'score_a':20,
				  'op':'peterparker',
				  'comments':[]},

				 {'_id':3,
			       	  'title':'Subscription Hell',
				  'link':'https://techcrunch.com/2018/05/06/subscription-hell/',
				  'score_a':15,
				  'op':'brucewayne',
				  'comments':[]},

			 	 {'_id':4,
			       	  'title':'Awesome Hyperledger',
				  'link':'https://github.com/skcript/awesome-hyperledger',
				  'score_a':112,
				  'op':'tonystark',
				  'comments':[]},

				 {'_id':5,
			       	  'title':'ODNS',
				  'link':'https://odns.cs.princeton.edu/',
				  'score_a':55,
				  'op':'brucebanner',
				  'comments':[]},

				 {'_id':6,
			       	  'title':'Birds of a Feather',
				  'link':'https://www.topic.com/birds-of-a-feather',
				  'score_a':39,
				  'op':'clarkkent',
				  'comments':[]},

				 {'_id':7,
			       	  'title':'While Loops JavaScript',
				  'link':'https://codeburst.io/june-14-2017-while-loops-vs-if-loops-568cc635e43e',
				  'score_a':48,
				  'op':'peterparker',
				  'comments':[]},

				 {'_id':8,
			       	  'title':'Forging Intimacy',
				  'link':'https://www.theparisreview.org/blog/2018/05/04/forging-intimacy/',
				  'score_a':14,
				  'op':'clarkkent',
				  'comments':[]},

				 {'_id':9,
			       	  'title':'New Clues to How the Brain Maps Time',
				  'link':'https://www.quantamagazine.org/new-clues-to-how-the-brain-maps-time-20160126/',
				  'score_a':12,
				  'op':'clarkkent',
				  'comments':[]},

				 {'_id':10,
			       	  'title':'MIT Detonation System',
				  'link':'http://massis.lcs.mit.edu/telecom-archives/archives/technical/western-union-tech-review/17-1/p032.htm',
				  'score_a':1,
				  'op':'brucewayne',
				  'comments':[]},

				 {'_id':11,
			       	  'title':'Bitcoin Banknotes',
				  'link':'http://researchly.leobosankic.com/2018/05/06/bitcoin-banknotes-living-old-world/',
				  'score_a':2,
				  'op':'peterparker',
				  'comments':[]},

				 {'_id':12,
			       	  'title':'KimDotCom Tweet',
				  'link':'https://twitter.com/KimDotcom/status/993256750437416960',
				  'score_a':5,
				  'op':'tonystark',
				  'comments':[]},

				 {'_id':13,
			       	  'title':'EchoThread for Slack',
				  'link':'https://hello.echothread.com/',
				  'score_a':140,
				  'op':'brucewayne',
				  'comments':[]},

				 {'_id':14,
			       	  'title':'Subscribe with Google',
				  'link':'https://blog.google/topics/google-news-initiative/introducing-subscribe-google/',
				  'score_a':6,
				  'op':'brucebanner',
				  'comments':[]},

				 {'_id':15,
			       	  'title':'The Oregon Trail',
				  'link':'https://en.wikipedia.org/wiki/The_Oregon_Trail',
				  'score_a':1,
				  'op':'peterparker',
				  'comments':[]}])

users.insert([{'_id':1,
		       'user':'clarkkent',
		       'karma':170},
		      {'_id':2,
		       'user':'peterparker',
		       'karma':71},
		      {'_id':3,
		       'user':'brucewayne',
		       'karma':156},
		      {'_id':4,
		       'user':'tonystark',
		       'karma':117},
		      {'_id':5,
		       'user':'brucebanner',
		       'karma':61}])

# Action 1: steverogers creates an account
users.insert({'_id':6,
		      'user':'steverogers',
		      'karma':0})

# Action 2: steverogers visits the homepage, returning information on the top 10 articles
articles.find().sort([('score_a',-1)]).limit(10)

# Action 3: steverogers clicks on the first article on the page, returning its link
articles.find({'_id':13},{'link':1,'_id':0})

# Action 4: steverogers upvotes the article
articles.update({'_id':13},{'$inc':{'score_a':1}})

# Action 5: steverogers comments on the article
articles.update({'_id':13},{'$push':{'comments':{'text':'cool!',
												 'user':'steverogers',
												 'score_c':0}}})

# Action 6: steverogers posts his own article
articles.insert_one({'_id':16,
	 				 'title':'MongoDB',
					 'link':'https://www.mongodb.com/',
					 'score_a':1,
					 'op':'steverogers',
					 'comments':[]})

# Action 7: clarkkent upvotes on steverogers' post
articles.update({'_id':16},{'$inc':{'score_a':1}})

# Action 8: steverogers checks his karma
users.find({'_id':6},{'karma':1,'_id':0})
