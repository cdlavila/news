from flask import request, jsonify, Blueprint
from app.services import news_service

news_router = Blueprint('news_routes', __name__)


@news_router.route('/', methods=['POST'])
def create_news():
    try:
        payload = request.get_json()
        data = {
            'title': payload.get('title'),
            'description': payload.get('description'),
            'author': payload.get('author'),
        }
        created_news = news_service.crate_news(data)
        return jsonify({
            'data': created_news,
            'message': 'News article created successfully'
        }), 201
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while creating news article',
        }), 500


@news_router.route('/', methods=['GET'])
def get_all_news():
    try:
        all_news = news_service.get_all_news()
        return jsonify({
            'data': all_news,
            'message': 'News articles retrieved successfully'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while retrieving news articles'
        }), 500


@news_router.route('/<string:id>', methods=['GET'])
def get_one_news(id):
    try:
        news = news_service.get_one_news(id)
        if news is None:
            return jsonify({
                'error': 'Not found',
                'message': 'News article not found'
            }), 404
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


@news_router.route('/<string:id>', methods=['PATCH'])
def update_news(id):
    try:
        news = news_service.get_one_news(id)
        if news is None:
            return jsonify({
                'error': 'Not found',
                'message': 'News article not found'
            }), 404
        payload = request.get_json()
        data = {
            'title': payload.get('title'),
            'description': payload.get('description'),
            'author': payload.get('author'),
        }
        result = news_service.update_news(id, data)
        if result is None:
            return jsonify({
                'error': 'Bad Request',
                'message': 'News article not updated'
            }), 400
        return jsonify({
            'data': result.get('news'),
            'message': 'News article updated successfully'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while updating news article'
        }), 500


@news_router.route('/<string:id>', methods=['DELETE'])
def delete_news(id):
    try:
        news = news_service.get_one_news(id)
        if news is None:
            return jsonify({
                'error': 'Not found',
                'message': 'News article not found'
            }), 404

        result = news_service.delete_news(id)
        if result is None:
            return jsonify({
                'error': 'Bad Request',
                'message': 'News article not deleted'
            }), 400
        return jsonify({
            'message': 'News article deleted successfully'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while deleting news article'
        }), 500
