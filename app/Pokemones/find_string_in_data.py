"""this module contains some functions for item 1 from houm challenge"""

def get_key_data(data: dict, key: str):
    """this function get value in a key from data, return a list with values of key required"""

    data_key = [element[key] for element in data["results"]]

    return data_key


def find_string_in_name(string_to_find: str, data: dict, times=1):
    """this function return a data of a string validation in name"""

    data_with_condition=[]

    for element in data:

        if string_to_find in element:
            if times>1:
                if element.count(string_to_find) >= times:
                    data_with_condition.append(element)
            else:
                data_with_condition.append(element)
    return data_with_condition




