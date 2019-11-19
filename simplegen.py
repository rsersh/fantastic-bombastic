"""Bite 214. Simple generator that counts down from 100 to 1 """
def countdown():
    """Write a generator that counts from 100 to 1"""
    for i in range(100,1,-1):
        yield(i)

c = countdown()
for i in range(5):
    print(next(c))
