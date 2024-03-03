from flask import Flask
import os
from flask_mail import Mail
from redis import Redis
import rq

mail = Mail()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py", silent=True)
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass
    mail.init_app(app)

    # Redis initialization
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue(app.config['QUEUES'][0], connection=app.redis)

    from .routes import dashboard
    app.register_blueprint(dashboard.bp)

    from .services import redis_tasks
    app.register_blueprint(redis_tasks.bp)

    return app