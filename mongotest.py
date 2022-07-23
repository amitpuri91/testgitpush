import pymongo

client = pymongo.MongoClient("mongodb://amitpuri91:optimum4@ac-pg0pjt2-shard-00-00.zxhu9g4.mongodb.net:27017,ac-pg0pjt2-shard-00-01.zxhu9g4.mongodb.net:27017,ac-pg0pjt2-shard-00-02.zxhu9g4.mongodb.net:27017/?ssl=true&replicaSet=atlas-af5ah7-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

print(db)

d={"name":"amit","email":"amit@gmail.com",
   "surname":"kumar"}

d={"name":"amit","email":"amit@gmail.com",
   "surname":"kumar"}

d={"name":"amit","email":"amit@gmail.com",
   "surname":"kumar"}

db1=client['mongotest']
coll=db1['tes1']
coll.insert_one(d)


