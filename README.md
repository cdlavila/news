# News
REST API for a news article app created with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [MongoDB](https://www.mongodb.com/).
<br>
<br>
It has the following endpoints:
- `POST /api/v1/news` - Create a new news article
- `GET /api/v1/news` - Get all news articles
- `GET /api/v1/news/<id>` - Get a specific news article
- `PATCH /api/v1/news/<id>` - Update specific fields of a news article
- `DELETE /api/v1/news/<id>` - Delete a news article

## Installation
1. Clone the repository
2. Copy `.env.example` to `.env` and fill in the values
3. Run `docker-compose up -d`
4. Run `python3 -m venv venv`
5. Run `source venv/bin/activate`
6. Run `pip3 install -r requirements.txt`
7. Run `python3 app.py`

## Linter
1. Run `pylint filename.py` to run the linter on a specific file
2. Run `pylint foldername` to run the linter on a specific folder
