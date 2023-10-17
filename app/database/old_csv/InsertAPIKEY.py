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
collection_users= db["users"]

# Create index on 'Title' and 'book_id' fields
collection_users.create_index([('Id', pymongo.ASCENDING)])

# Loop through ratings and update book_id
documents = collection_users.find()

for document in documents:
    collection_users.update_one(
        {'_id': document['_id']},  # Specify the document by its '_id' field
        {'$set': {'api_key': ''}}  # Add the new column with its value
    )

print("END OF THE SCRIPT.....")
