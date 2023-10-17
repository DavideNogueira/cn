from pymongo import MongoClient
import csv

DOMAIN = 'localhost'
PORT = 27018

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

db.drop_collection("books_data")
db.drop_collection("books_rating")
db.drop_collection("users")

db.create_collection("books_data")
file = open("books_data.csv", encoding="utf-8")
csvreader = csv.reader(file, delimiter=',')
headings = next(csvreader)

books_data = []
i = 0


for row in csvreader:
    data = {
        'Id': int(row[0].strip()),
        'Title': row[1].strip(),
        '_id': row[2].strip(),
        'authors': row[3].strip(),
        'categories': row[4].strip(),
        'description': row[5].strip(),
        'image': row[6].strip(),
        'infoLink': row[7].strip(),
        'previewLink': row[8].strip(),
        'publishedDate': row[9].strip(),
        'publisher': row[10].strip(),
        'ratingsCount': row[11].strip(),
    }

    # append
    books_data.append(data)
    i = i + 1

db.books_data.insert_many(books_data)

file.close()

db.create_collection("books_rating")
books_rating = db["books_rating"]
file2 = open("books_rating.csv")
csvreader2 = csv.reader(file2, delimiter=',')
headings2 = next(csvreader2)

reviews = []

for row in csvreader2:
    data2 = {
        'Id': row[0].strip(),
        'Price': row[1].strip(),
        'Title': row[2].strip(),
        'User_id': row[3].strip(),
        'book_id': int(row[4].strip()),
        'profileName': row[5].strip(),
        'review/helpfulness': row[6].strip(),
        'review/score': row[7].strip(),
        'review/summary': row[8].strip(),
        'review/text': row[9].strip(),
        'review/time': row[10].strip(),
    }

    # append
    reviews.append(data2)

books_rating.insert_many(reviews)

file2.close()

users = db.create_collection("users")

users_table = db["users"]
file3 = open("users.csv")
csvreader3 = csv.reader(file3, delimiter=',')
headings3 = next(csvreader3)

usersArray = []

for row in csvreader3:
    data3 = {
        'Id': int(row[0].strip()),
        'admin': row[1].strip(),
        'api_key': row[2].strip(),
        'password': row[3].strip(),
        'username': row[4].strip(),
    }

    # append
    usersArray.append(data3)

users_table.insert_many(usersArray)

file3.close()

print('Done')