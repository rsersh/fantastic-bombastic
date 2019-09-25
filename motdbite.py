#! /usr/bin/python3

workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       Then check if this title cased day is in the given workout_schedule dict.

       If it is retrieve the workout (value), if not raise a KeyError.

       Return the chill variable if it's a rest day (Saturday / Sunday),
       else return the go_train variable with the workout interpolated.

       Examples:
       - if day is Saturday -> return 'Chill out!'
       - if day is Thursday -> return 'Go train Legs'
       - if day is Sunday -> return 'Chill out!'
       - if day is Monday -> return 'Go train Chest+biceps'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    day = day.capitalize()
    if day not in workout_schedule.keys():
        raise KeyError('Problem with day as entered.')
    if day in workout_schedule.keys(): 
        use_this = workout_schedule[day]  
        if day == 'Saturday' or day == 'Sunday':
            return chill
        else:
            return go_train.format(use_this)
    pass


day = 'Thursday'
try:
    test = get_workout_motd(day)
    print(test)
except Exception as err:
    print('An Exception happened: ' + str(err))

day = 'Saturday'
try:
    test = get_workout_motd(day)
    print(test)
except Exception as err:
    print('An Exception happened: ' + str(err))

day = 'Funday'
try:
    test = get_workout_motd(day)
    print(test)
except Exception as err:
    print('An Exception happened: ' + str(err))
