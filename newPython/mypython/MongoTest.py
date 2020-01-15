from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('localhost', 27017)
db = client.test
collection = db.lendings.find()

for item in collection:
    print(item)

pprint(db.categories.find())

for db in client.list_databases():
    print(db)



# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)