import os
from flask import Flask
from dotenv import load_dotenv
from src.routes import news_route

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Set up environment variables
app.config['PORT'] = os.getenv('PORT')
app.config['MONGO_HOST'] = os.getenv('MONGO_HOST')
app.config['MONGO_PORT'] = os.getenv('MONGO_PORT')
app.config['MONGO_DATABASE'] = os.getenv('MONGO_DATABASE')
app.config['MONGO_USER'] = os.getenv('MONGO_USER')
app.config['MONGO_PASSWORD'] = os.getenv('MONGO_PASSWORD')


# Create routes
@app.route("/")
def hello_world():
    return "<p>Welcome to the news REST API!</p>"


# Register routes
app.register_blueprint(news_route.routes)


# Run Flask app
if __name__ == "__main__":
    app.run(debug=True, port=app.config['PORT'])
