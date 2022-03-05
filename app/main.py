from get_data import get_api_data
from find_string_in_data import get_key_data, find_string_in_name

from api_vars import POKEMON_ENDPOINT, API_URL

if __name__ == '__main__':

    all_pokemon = get_api_data(API_URL, POKEMON_ENDPOINT)

    pokemon_names = get_key_data(all_pokemon,"name")

    find_at= find_string_in_name("at",pokemon_names)

    find_a = find_string_in_name("a",find_at,2)

    # print(find_at)
    print(len(find_a))

    # names_with_condition=[]

    # for pokemon_name in pokemon_names:
    #     if "at" in pokemon_name and pokemon_name.count("a") >= 2:
    #         names_with_condition.append(pokemon_name)
    # print(pokemon_names)
    # print(len(names_with_condition))
    
        

    

