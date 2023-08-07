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


dbs = client.list_database_names()
print("Databases: ", dbs)
test_db = client.test_db
collections = test_db.list_collection_names()
print("Collections in test_db:", collections)