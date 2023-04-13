from bson import ObjectId
from flask import request, jsonify
from app.database import db


def create():
    try:
        """Create a new news article"""
        payload = request.get_json()
        data = {
            'title': payload.get('title'),
            'description': payload.get('description'),
            'author': payload.get('author'),
        }
        result = db['news'].insert_one(data)
        data['_id'] = str(result.inserted_id)
        return jsonify({
            'data': data,
            'message': 'News article created successfully'
        }), 201
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while creating news article',
        }), 500


def get_all():
    try:
        """Get all news articles"""
        news = list(db['news'].find())
        for n in news:
            n['_id'] = str(n['_id'])
        return jsonify({
            'data': news,
            'message': 'News articles retrieved successfully'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while retrieving news articles'
        }), 500


def get_one(id):
    try:
        """Get a single news article"""
        news = db['news'].find_one({'_id': ObjectId(id)})
        if news is None:
            return jsonify({
                'error': 'Not found',
                'message': 'News article not found'
            }), 404
        news['_id'] = str(news['_id'])
        return jsonify({
            'data': news,
            'message': 'News article retrieved successfully'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while retrieving news article'
        }), 500


def update(id):
    try:
        """Update a news article"""
        payload = request.get_json()

        news = db['news'].find_one({'_id': ObjectId(id)})
        if news is None:
            return jsonify({
                'error': 'Not found',
                'message': 'News article not found'
            }), 404
        news['_id'] = str(news['_id'])

        data = dict()
        for key, value in payload.items():
            if value:
                data[key] = value
                news[key] = value
        result = db['news'].update_one({'_id': ObjectId(id)}, {'$set': data})

        if result.modified_count == 1:
            return jsonify({
                'data': news,
                'message': 'News article updated successfully'
            }), 200
        else:
            return jsonify({
                'error': 'Bad Request',
                'message': 'News article not updated'
            }), 400
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while updating news article'
        }), 500


def delete(id):
    try:
        """Delete a news article"""
        news = db['news'].find_one({'_id': ObjectId(id)})
        if news is None:
            return jsonify({
                'error': 'Not found',
                'message': 'News article not found'
            }), 404

        result = db['news'].delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 1:
            return jsonify({
                'message': 'News article deleted successfully'
            }), 200
        else:
            return jsonify({
                'error': 'Bad Request',
                'message': 'News article not deleted'
            }), 400
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while deleting news article'
        }), 500
