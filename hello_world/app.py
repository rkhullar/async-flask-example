from hello_world.core import HelloWorld
from quart import Blueprint, Quart, jsonify, request
import logging
import os

api = Blueprint('api', __name__)
core = HelloWorld(app_env=os.environ.get('APP_ENV', 'sbx'))


@api.route('/', methods=['GET'])
async def index_get():
    welcome = dict(message='hello world', status='ok')
    return jsonify(welcome)


@api.route('/hello', methods=['POST'])
async def hello_post():
    logging.info('test hello')
    body = await request.get_json()
    result = await core.hello(message=body['message'], count=body['count'], delay=1)
    return jsonify(result)


def create_app(mode: str = None):
    mode = mode or os.environ.get('FLASK_CONFIG', 'sbx')
    app = Quart(__name__)
    # app.config.from_object(config[mode])
    app.register_blueprint(api, '/api')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
