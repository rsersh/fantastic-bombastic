"""Bite 21. Query a nested data structure

Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names (should work for other grep too)
Sort the models (values) alphabetically

See the docstrings and tests for more details. Have fun!

Update 18th of Sept 2018: as concluded in the forum it is better to pass the cars dict
into each function to make its scope local.


"""
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return (', ').join(cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [cars[k][0] for k in cars.keys()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    model_match = []
    for model_list in cars.values():
        for model in model_list:
            if grep.lower() in model.lower():
                model_match.append(model)
    model_match.sort()
    return list(model_match)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return { k:sorted(v) for k,v in cars.items() }


#print(get_all_jeeps())
#print(get_first_model_each_manufacturer())
matchlist = get_all_matching_models(cars, 'CO')
print(matchlist)
#modelsortdict = sort_car_models()
#print(modelsortdict)
