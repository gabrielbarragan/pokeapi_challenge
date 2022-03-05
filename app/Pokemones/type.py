from api_vars import API_URL

from Pokemones.data import get_api_data

"""this module contains the functions for all corresponds to item 3 from houm challenge"""

def get_ids_smaller(data: dict, key: str, max_id: int):
    """this function get pokemons ids smaller max_id when receive the data from endpoint type"""

    data_key = [element["pokemon"]['url'] for element in data[key]]
    data_urls= []
    for data in data_key:
        id= int((data.replace(API_URL+"pokemon/","")).replace("/",""))
        if id <=max_id:
            data_urls.append(id)
    return data_urls

def get_weights_in_pokemon_of_type(type: str, max_number_of_pokemon: int):
    """this function receive an type (string) of pokemon 
        return a data with pokemons from this type"""

    data_type= get_api_data(API_URL+"type/"+type)
    
    pokemon_of_type = get_ids_smaller(data_type, "pokemon",max_number_of_pokemon)
    all_weights=[]

    for id in pokemon_of_type:

        one_pokemon = get_api_data(API_URL+"pokemon/"+str(id))
        all_weights.append(one_pokemon["weight"])
        all_weights.sort()

    max_weight, min_weight = all_weights[0], all_weights[len(all_weights)-1]

    return [max_weight, min_weight]
