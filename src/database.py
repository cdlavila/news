import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to the MongoDB instance
client = MongoClient(
    host=os.getenv('MONGO_HOST'),
    port=int(os.getenv('MONGO_PORT')),
    username=os.getenv('MONGO_USER'),
    password=os.getenv('MONGO_PASSWORD'))

# Get the database
print('Connection to MongoDB successful')
db = client[os.getenv('MONGO_DATABASE')]
