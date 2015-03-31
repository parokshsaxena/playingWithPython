from __future__ import absolute_import
from celery import Celery

cele = Celery("celeryProject",backend='amqp',broker='amqp://guest@localhost//')
cele.config_from_object('celeryProject.celeryconfig')

if __name__ == '__main__':
    cele.start()