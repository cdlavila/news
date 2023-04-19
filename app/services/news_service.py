from app.database import db
from bson import ObjectId


def crate_news(data):
    created_news = db['news'].insert_one(data)
    data['_id'] = str(created_news.inserted_id)
    return data


def get_all_news():
    all_news = list(db['news'].find())
    for news in all_news:
        news['_id'] = str(news['_id'])
    return all_news


def get_one_news(id):
    news = db['news'].find_one({'_id': ObjectId(id)})
    if news is None:
        return None
    news['_id'] = str(news['_id'])
    return news


def update_news(id, data):
    result = db['news'].update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count == 0:
        return None
    news = db['news'].find_one({'_id': ObjectId(id)})
    news['_id'] = str(news['_id'])
    return {'updated_count': result.modified_count, 'news': news}


def delete_news(id):
    result = db['news'].delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 0:
        return None
    return {'deleted_count': result.deleted_count}
