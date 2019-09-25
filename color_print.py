#! /usr/bin/python3
# to be run with Python 3.7

VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        color = input("Please enter a color or 'quit': ")
        if color.lower() == 'quit':
            print('bye')
            break
        if color.lower() not in VALID_COLORS:
            print('Not a valid color')
            continue
        else:
            print(color.lower())
        pass

print_colors()


