from flask import Flask
from app.config import Config
from app.routers import news_router

# Create Flask app
app = Flask(__name__)

# Set up environment variables
app.config.from_object(Config)


# Create main routers
@app.route("/")
def root():
    return "<p>News server running!</p>"


@app.route("/api/v1")
def say_welcome_api():
    return "<p>Welcome to the news REST API V1!</p>"


# Register other routers
app.register_blueprint(news_router.routes)


# Run Flask app
if __name__ == "__main__":
    app.run(debug=True, port=app.config['PORT'])
