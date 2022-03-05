from Pokemones.get_data import get_api_data
def get_egg_group_url(specie_data):
    """This function get egg groups url from give specie and return a list with egg_groups"""

    egg_group = [egg_group["url"] for egg_group in specie_data["egg_groups"] ]

    return egg_group

def get_egg_group_name(specie_data):
    """This function get egg groups name from give specie and return a list with egg_groups"""

    egg_group = [egg_group["name"] for egg_group in specie_data["egg_groups"] ]

    return egg_group

def get_pokemon_species_from_group(egg_group_data):
    """this function return a list with pokemon species from a egg group"""

    pokemon_specie = [specie["name"] for specie in egg_group_data["pokemon_species"] ]

    return pokemon_specie
def count_species(list_group_url):
    """this function combine the pokemon species from a pokemon, remove duplicates and return total quantity of species """

    egg_groups_data=[]

    for egg_group_url in list_group_url:
         egg_groups_lists= get_pokemon_species_from_group(get_api_data(egg_group_url))
         for specie in egg_groups_lists:
             egg_groups_data.append(specie)
    
    
    return len(set(egg_groups_data))




