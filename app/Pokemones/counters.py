from Pokemones.find_string_in_data import find_string_in_name, get_key_data
from Pokemones.data import get_api_data
from Pokemones.egg_group import get_egg_group_url, count_species


def count_names(data,first_string: str="",first_string_times:int=1, second_string: str="", second_string_times:int=0):
    """get a length of data given two strings to find in order"""
    names = get_key_data(data,"name")

    find_first_string= find_string_in_name(first_string,names,first_string_times)

    find_second_string = find_string_in_name(second_string,find_first_string,second_string_times)

    return len(find_second_string)

def species_to_procreate(specie_endpoint: str):
    """this function return quantity of species can be couple with raichu"""
    data_specie = get_api_data(specie_endpoint)
    
    egg_groups_url = get_egg_group_url(data_specie)
    
    quantity_species_procreate= count_species(egg_groups_url)

    return quantity_species_procreate