"""Rewrite a for loop using recursion
Although you have to be careful using recursion it is one of those concepts you want to at least understand. It's also commonly used in coding interviews :)

In this beginner Bite we let you rewrite a simple countdown for loop using recursion. See countdown_for below, it produces the following output:

    $ python countdown.py
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    time is up

You will be tested on having the same output, making it work with another start value, and of course if you used recursion. Have fun!
#recursion #reverse
"""
def trythis(startvalue):
    if startvalue == 0:
        print('time is up')
        return
    print(startvalue)
    if startvalue > 0:
        trythis(startvalue-1)

trythis(10)    

