from pymongo import MongoClient
from src.config import Config

# Connect to the MongoDB instance
client = MongoClient(
    host=Config.MONGO_HOST,
    port=Config.MONGO_PORT,
    username=Config.MONGO_USER,
    password=Config.MONGO_PASSWORD,
)

# Get the database
print('Connection to MongoDB successful')
db = client[Config.MONGO_DATABASE]
