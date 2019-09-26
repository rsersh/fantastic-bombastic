"""
Sum n numbers

    Write a function that can sum up numbers:

        It should receive a list of n numbers.
        If no argument is provided, return sum of numbers 1..100.
        Look closely to the type of the function's default argument ...

    Have fun!
import inspect

"""
# default args, None, range, sum
def sum_numbers(numbers=None):
    if numbers is None:
        numbers = []
        for i in range(101):
            numbers.append(i)
    return sum(numbers)
    pass

result = sum_numbers([])
print(result)
result = sum_numbers([15,22,18,43])
print(result)
result = sum_numbers()
print(result)
