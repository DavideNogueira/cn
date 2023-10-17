from pymongo import MongoClient
import csv

CONNECTION_URL = 'mongodb+srv://root:root@cloudcomputingcluster.8q0ke5i.mongodb.net'
DB_NAME = 'CloudComputing23'

print("Connecting to database.....")

client = MongoClient(CONNECTION_URL, serverSelectionTimeoutMS=5000)

print("Connected.....")
print("Proceeding with the insertions.....")

db = client[DB_NAME]

db.books_data.drop()
with open("books_data.csv") as file:
    csvreader = csv.DictReader(file)
    books_data = [{"Id": i, **row} for i, row in enumerate(csvreader)]
db.books_data.insert_many(books_data)

db.books_rating.drop()
with open("books_rating.csv") as file:
    csvreader = csv.DictReader(file)
    books_rating = list(csvreader)
db.books_rating.insert_many(books_rating)

db.users.drop()
users_names = ["admin1" , "admin2" , "user1", "user2", "user3"]
users_array = [
    {"Id": i, "name": name, "admin": (i in [0, 1])} for i, name in enumerate(users_names)
]
db.users.insert_many(users_array)

print('Done')