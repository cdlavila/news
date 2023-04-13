import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()


class Config:
    PORT = os.getenv('PORT')
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_PORT = int(os.getenv('MONGO_PORT'))
    MONGO_DATABASE = os.getenv('MONGO_DATABASE')
    MONGO_USER = os.getenv('MONGO_USER')
    MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
