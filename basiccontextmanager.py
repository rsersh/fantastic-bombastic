"""Bite 20. Write a context manager
Write a context manager to roll back a transaction on the given Account class.
There are two special (aka dunder) methods you need to define to create a context 
manager (there is also a convenient decorator - see Bite 88).

The purpose of the context manager is to roll back any transaction that will make 
the balance go below 0 (debt != cool). The rest of the class is already defined 
so you can focus on the context manager part.

See the tests for more detail. Good luck and keep calm and code in Python!
context managers dunders operator overloading with statement
"""

class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        while self.balance < 0:
            del _transactions[-1]
