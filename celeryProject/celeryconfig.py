from kombu import Exchange,Queue
from celery.schedules import crontab

import celeryProject.startTask
BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_IMPORTS = ("celeryProject.addTask","celeryProject.multiplyTask","celeryProject.startTask")
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

CELERYBEAT_SCHEDULE = {
    'my-scheduler' : {
        'task' : 'celeryProject.startTask.start',
        'schedule' : crontab(minute='*/1'),
        'args' : [5]
        #'args' : [2,5]
    },
}

CELERY_QUEUES = (
    Queue(name="addQueue",Exchange="addQueueExc",routing_key="addQueue"),
    Queue(name="multQueue",Exchange="multQueue",routing_key="multQueue"),
    Queue(name="printQueue",Exchange="printQueue",routing_key="printQueue"),
)

CELERY_ROUTES = {
    'celeryProject.addTask.add' : {
        'queue' : 'addQueue'
    },
    'celeryProject.addTask.printNum' : {
       'queue' : 'printQueue'
    },
    'celeryProject.multiplyTask.multiply' : {
        'queue' : 'multQueue'
    },
    'celeryProject.startTask.start' : {
        'queue' : 'addQueue'
    },

}