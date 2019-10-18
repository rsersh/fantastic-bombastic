"""Write a user validation function

    Create a function that takes a username and checks for a valid user:

        The username is in USERS,
        the user is not expired, and
        the user has the ADMIN role.

    If those 3 conditions are met return SECRET.

    If one of the conditions is not True raise an exception you define yourself: UserDoesNotExist, UserAccessExpired and UserNoPermission respectively. Check out the tests for more detail.

    Have fun and keep calm and code in Python!
    
    classes exception handling namedtuple
"""
from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

class UserDoesNotExist(Exception):
    """Exception raised when User is not found in USERS"""

class UserAccessExpired(Exception):
    """Exception raised when User's expired field is set to False"""

class UserNoPermission(Exception):
    """Exception raised when User is not 'admin'"""

def get_secret_token(username):
    index = -999
    userlist = list(USERS)
    for i in range(len(userlist)):
        if userlist[i].name.lower() == username.lower():
            index = i
    if index != -999:
        user = userlist[index]
    else:
        raise UserDoesNotExist
    if user.expired is True:
        raise UserAccessExpired
    if user.role  != "admin":
        raise UserNoPermission
    else:
        return SECRET


message = get_secret_token('PyBites')
print(message)
"""
message = get_secret_token('julian')
print(message)
message = get_secret_token('bob')
print(message)
message = get_secret_token('Tim')
print(message)
"""
