__author__ = 'paroksh.saxena'

from celeryProject.addTask import add
from celeryProject.multiplyTask import multiply

add.delay(2,4)
multiply.delay(2,4)

