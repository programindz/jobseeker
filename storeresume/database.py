from pymongo import MongoClient
import os

client = MongoClient(f"{os.getenv("MONGODB")}")
resume_db = client['resumedb']
resume_collection = resume_db['applicantDetails']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
