from django.db import models

# Create your models here.
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.testdb

def find_document():
    post = db.user
    print("inside mongo: ",post.find_one())
    return post.find_one()
    