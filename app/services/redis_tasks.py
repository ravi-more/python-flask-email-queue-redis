from flask import current_app, Blueprint
from .email import (send_email)

from rq import Connection, Worker
import redis

bp = Blueprint("redis_task", __name__)


@bp.cli.command('run_worker')
def run_worker():
    redis_url = current_app.config['REDIS_URL']
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(current_app.config['QUEUES'])
        worker.work()


def enqueue_email_to_redis(recipients, subject=None,  text_body=None, html_body=None):
    '''function add email to queue send mails using rq'''
    current_app.task_queue.enqueue(send_email,
                                   subject=subject,
                                   recipients=recipients,
                                   text_body=text_body,
                                   html_body=html_body)
