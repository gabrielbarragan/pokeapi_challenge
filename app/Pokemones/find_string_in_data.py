"""this module contains some functions for item 1 from houm challenge"""

def get_key_data(data: dict, key: str):
    """this function get value in a key from data, return a list with values of key required"""
    
    data_key = [element[key] for element in data["results"]]
    if data_key is not None or data_key != "":
        
        return data_key
    
    else:
        raise ValueError("No se ha podido obtener datos de la llave resultados para la data proporcionada en la función get_key_data")


def find_string_in_name(string_to_find: str, data: dict, times: int=0):
    """this function return a data of a string validation in data name"""

    data_with_condition=[]
    if data is not None or data != "" or type(data) is not dict:

        for element in data:
            if times==0:
                data_with_condition.append(element)
            elif times>=1:
                if string_to_find in element:
            
                    if element.count(string_to_find) >= times:
                        data_with_condition.append(element)   

        return data_with_condition
    else:
        raise ValueError("No es posible buscar las cadenas dadas ya que la data está vácia (función: find_string_in_name)")




