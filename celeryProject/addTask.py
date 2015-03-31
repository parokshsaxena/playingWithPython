__author__ = 'paroksh.saxena'

from celeryProject.celeryFile import cele

@cele.task
def add(num1,num2):
    num3 = num1 + num2
    print("Sending from add to print")
    body = "Add result : " + str(num3)
    printNum.delay(body)

@cele.task
def printNum(num1):
    print(num1)

# #add(3,4)