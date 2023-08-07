from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import pprint
import os

load_dotenv(find_dotenv())


password = os.environ.get("MONGODB_PWD")
uri = f"mongodb+srv://mubarakmayyeri:{password}@cluster0.3hujcn7.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# dbs = client.list_database_names()
# print("Databases: ", dbs)
# test_db = client.test_db
# collections = test_db.list_collection_names()
# print("Collections in test_db:", collections)



def insert_document(document):
    collection = client.test_db.test_collection
    collection.insert_one(document)
    print("Document inserted succesfully")

# doc = {
#     "Name": "Mubarak M",
#     "Role": "Python Dev"
# }

# insert_document(doc)

db = client.school
studnet_collection = db.students

# first_names = ["Alice", "Bob", "Charlie", "Diana", "Ella"]
# last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
# ages = [18, 23, 20, 19, 22]

# docs = []

# for f_name, l_name, age in zip(first_names, last_names, ages):
#     doc = {"first_name": f_name, "last_name":l_name, "age": age}
#     docs.append(doc)


def insert_document(documents, collection):
    collection.insert_many(documents)
    print("Documents inserted succesfully")

# insert_document(docs, collection)

printer = pprint.PrettyPrinter()
def get_documents(collection):
    cursor = collection.find()

    for i in cursor:
        printer.pprint(i)

# get_documents(collection)

def get_diana(collection):
    diana = collection.find_one({"first_name": "Diana"})
    printer.pprint(diana)

# get_diana(studnet_collection)

def find_count():
    count = studnet_collection.count_documents(filter={})
    return count

# print("Number of students: ", find_count())


def student_by_id(student_id):
    from bson.objectid import ObjectId

    _id = ObjectId(student_id)

    student = studnet_collection.find_one({"_id": _id})
    printer.pprint(student)


# student_by_id("64d09c52b85fcd3cd2d5c420")

def get_age_range(min_age, max_age):
    query = {
        "$and":[
            {'age':{'$gte' : min_age}},
            {'age':{'$lte': max_age}}
    ]}

    students = studnet_collection.find(query).sort("age")

    for st in students:
        printer.pprint(st)

# get_age_range(19, 25)

def project_columns():
    columns = {'_id': 0, 'first_name': 1, "age": 1}

    students = studnet_collection.find({}, columns)

    for st in students:
        printer.pprint(st)

# project_columns()