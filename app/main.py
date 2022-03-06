from Pokemones.data import get_api_data, get_specie_endpoint
from Pokemones.type import get_weights_in_pokemon_of_type
from Pokemones.counters import count_names
from Pokemones.counters import species_to_procreate

from api_vars import POKEMON_ENDPOINT, API_URL

if __name__ == '__main__':
    #obteniendo el endpoind para la especie de raichu
    RAICHU_SPECIE_ENDPOINT = get_specie_endpoint("raichu")

    #se obtiene la data de todos los pokemon
    all_pokemon = get_api_data(API_URL+ POKEMON_ENDPOINT)

    #1) contamos los nombres que contienen at y dos a's en el nombre
    count_strings_in_names= count_names(all_pokemon,"at",1,"a",2) 

    #2) contamos la cantidad de especies que pueden procrear con Raichu
    species_to_couple = species_to_procreate(RAICHU_SPECIE_ENDPOINT)
    

    #3) obtenemos el peso máximo y mínimo de un tipo de pokemon dado un id máximo.
    pokemon_type= "fighting"
    max_and_min_weight = get_weights_in_pokemon_of_type(pokemon_type,151)


    print(f'En total hay {species_to_couple} de pokemon que pueden procrear con Raichu')
    print (f'El peso máximo y el mínimo de los pokemones de tipo {pokemon_type} son: {max_and_min_weight} respectivamente')
    if count_strings_in_names is not None:
        print(f'En total hay {count_strings_in_names} pokemones que contienen en su nombre "at" y "a"')
    else:
        print("no se han podido contar los pokemones")





    
    
        

    

