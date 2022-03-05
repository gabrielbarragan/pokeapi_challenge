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

    #contamos los nombres según las condiciones
    count_strings_in_names= count_names(all_pokemon,"at",1,"a",2)
    print(f'En total hay {count_strings_in_names} pokemones que contienen en su nombre "at" y por lo menos 2 "a"')

    #contamos la cantidad de especies que pueden procrear con Raichu
    species_to_couple = species_to_procreate(RAICHU_SPECIE_ENDPOINT)
    print(f'En total hay {species_to_couple} de pokemon que pueden procrear con Raichu')

    #get pokemons of an specific type
    print (f'El peso máximo y el mínimo de los pokemones de tipo fighting es: {get_weights_in_pokemon_of_type("fighting",151)} respectivamente')





    
    
        

    

