from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import json
import pprint
import os

load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()

password = os.environ.get("MONGODB_PWD")
uri = f"mongodb+srv://mubarakmayyeri:{password}@cluster0.3hujcn7.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

# with open('mock_data\MOCK_DATA.json') as file:
#     file_data = json.load(file)


db = client.mock_db
collection = db.employees
# collection.insert_many(file_data)