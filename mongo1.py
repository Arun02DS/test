import pymongo

client = pymongo.MongoClient("mongodb+srv://arun:jango123@arun.wpyhw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" :"arun",
     "email":"arun02nnn",
      "surname":"negi"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)