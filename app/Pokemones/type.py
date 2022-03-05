from api_vars import API_URL

from Pokemones.data import get_api_data

"""this module has all the necessary functions to obtain some data from the endpoint type. This corresponds to point 3 of Houm's challenge."""

def get_ids_smaller(data: dict, key: str, max_id: int):
    """this function get pokemons ids smaller than max_id when receive the data from  type endpoint"""

    data_key = [element["pokemon"]['url'] for element in data[key]]
    data_urls= []
    for data in data_key:
        id= int((data.replace(API_URL+"pokemon/","")).replace("/",""))
        if id <=max_id:
            data_urls.append(id)
    return data_urls

def get_weights_in_pokemon_of_type(type: str, max_number_of_pokemon: int):
    """this function receives a pokemon type in string format and returns a data with pokemons of that type"""

    data_type= get_api_data(API_URL+"type/"+type)
    
    pokemon_of_type = get_ids_smaller(data_type, "pokemon",max_number_of_pokemon)
    all_weights=[]

    for id in pokemon_of_type:

        one_pokemon = get_api_data(API_URL+"pokemon/"+str(id))
        all_weights.append(one_pokemon["weight"])
        

    max_weight, min_weight = max(all_weights), min(all_weights)

    return [max_weight, min_weight]
