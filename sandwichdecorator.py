"""Bite 218. Create a sandwich decorator

After creating our Decorators and Context Managers learning path we 
realized we did not have a beginner decorator Bite, so here it is!

Complete the sandwich decorator which takes a function and 
prints === Upper bread slice === (defined in UPPER_SLICE) 
and === Lower bread slice === (defined in LOWER_SLICE) before 
and after calling the passed in function (func).

And voilà applying this decorator to add_ingredients you have your 
sandwich (see also the tests):

    >>> from sandwich import sandwich
    >>> @sandwich
    ... def add_ingredients(ingredients):
    ...     print(' / '.join(ingredients))
    ...
    >>> ingredients = ['bacon', 'lettuce', 'tomato']
    >>> add_ingredients(ingredients)
    === Upper bread slice ===
    bacon / lettuce / tomato
    === Lower bread slice ===

This is probably the easiest way to demo a decorator. Even so 
decorators can be confusing when you start using them so here is 
an article we wrote some time ago: Learning Python Decorators by Example.
"""
from functools import wraps

UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="
#ingredients = ['fried egg', 'tomato', 'cucumber']

def sandwich(func):
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    @wraps(func)
    def wrapped(*args, **kwargs):
 
        print(UPPER_SLICE)
        result = func(*args,**kwargs)
        print(LOWER_SLICE)
    return wrapped

@sandwich
def add_ingredients(ingredients):
    print(' / '.join(ingredients))

ingredients = ['bacon', 'lettuce', 'tomato']
add_ingredients(ingredients)
    
