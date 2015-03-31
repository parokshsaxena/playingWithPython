__author__ = 'paroksh.saxena'

from celeryProject.addTask import printNum

from celeryProject.celeryFile import cele

@cele.task
def multiply(num1,num2):
    print("sending from multiply to print " + str(num1) + " and " + str(num2))
    num3 = num1*num2
    if num3==0:
        print("Not sending to print")
    else:
        print "Multiple result :  " + str(num3)
