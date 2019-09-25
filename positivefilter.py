def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    newlist = []
    for num in numbers:
        if num > 0:
            if num % 2 == 0:
                newlist.append(num)
    return newlist
    pass
