from pymongo import MongoClient

client = MongoClient('mongodb+srv://khansink:q1w2e3r4@songscluster.kertk8u.mongodb.net/?retryWrites=true&w=majority')
resume_db = client['resumedb']
resume_collection = resume_db['applicantDetails']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)