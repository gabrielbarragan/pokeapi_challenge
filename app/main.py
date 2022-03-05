from Pokemones.get_data import get_api_data
from Pokemones.count_names import count_names

from api_vars import POKEMON_ENDPOINT, API_URL

if __name__ == '__main__':

    all_pokemon = get_api_data(API_URL, POKEMON_ENDPOINT)

    count_strings_in_names= count_names(all_pokemon,"at",1,"a",2)

    print(count_strings_in_names)
    
        

    

