from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ziyis.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

db.book.insert_one(doc)