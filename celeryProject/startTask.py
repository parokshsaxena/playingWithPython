__author__ = 'paroksh.saxena'

from celeryProject.celeryFile import cele
from celeryProject.addTask import add
from celeryProject.multiplyTask import multiply

@cele.task
def start(var):
    add.delay(2,4)
    multiply.delay(2,4)