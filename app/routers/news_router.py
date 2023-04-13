from flask import Blueprint
from app.controllers import news_controller

routes = Blueprint('news_routes', __name__, url_prefix='/api/v1/news')

routes.route('/', methods=['POST'])(news_controller.create)
routes.route('/', methods=['GET'])(news_controller.get_all)
routes.route('/<string:id>', methods=['GET'])(news_controller.get_one)
routes.route('/<string:id>', methods=['PATCH'])(news_controller.update)
routes.route('/<string:id>', methods=['DELETE'])(news_controller.delete)
