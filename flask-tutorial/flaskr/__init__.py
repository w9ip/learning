import os

from flask import Flask


def create_app(test_config=None):
    """
    Эта функция выполняет роль фабрики сконфигурированных инстансов Flask'а.

    :param test_config:
    :return: сконфигурированный инстанс Flask'а.
    """
    # создание и конфигурация экземпляра (app) Flask.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # загрузить конфигурацию экземпляра, если она существует и не тестируется.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # загрузить тестовую конфигурацию, если она была передана.
        app.config.from_mapping(test_config)

    # убедиться, что папка экземпляра существует.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # простая страница с приветствием.
    @app.route('/hello')
    def hello():
        return 'Hello, World'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
