import pymongo
from pymongo import MongoClient

DOMAIN = 'localhost'
PORT = 27017

print("Connecting to database.....")

'''
client = MongoClient(
    host=[str(DOMAIN) + ":" + str(PORT)],
    serverSelectionTimeoutMS=5000,
    username="root",
    password="root"
)
'''

uri = "mongodb+srv://CN:dwAf9cmr7BuwxlMG@cn-project.ftfm8oe.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

print("Connected.....")
print("Proceeding with the insertions.....")
db = client["CloudComputing23"]
collection_book = db["books_data"]
collection_ratings = db["books_rating"]

# Create index on 'Title' and 'book_id' fields
collection_book.create_index([('Title', pymongo.ASCENDING)])
collection_ratings.create_index([('Title', pymongo.ASCENDING)])
collection_ratings.create_index([('book_id', pymongo.ASCENDING)])

# Loop through ratings and update book_id
bulk_updates = []
session = client.start_session()
with session:
    for doc in collection_ratings.find({}, {'_id': 1, 'Title': 1}, no_cursor_timeout=True, session=session):
        book = collection_book.find_one({'Title': doc['Title']}, {'Id': 1})
        bulk_updates.append(pymongo.UpdateOne({'_id': doc['_id']}, {'$set': {'book_id': book['Id']}}))
        if len(bulk_updates) == 1000:
            collection_ratings.bulk_write(bulk_updates, session=session)
            bulk_updates = []
    if bulk_updates:
        collection_ratings.bulk_write(bulk_updates, session=session)

print("END OF THE SCRIPT.....")
