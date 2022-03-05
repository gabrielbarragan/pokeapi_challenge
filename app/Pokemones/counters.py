from Pokemones.find_string_in_data import find_string_in_name, get_key_data
from Pokemones.data import get_api_data
from Pokemones.egg_group import get_egg_group_url, get_pokemon_species_from_group


def count_names(data,first_string: str="",first_string_times:int=0, second_string: str="", second_string_times:int=0):
    """get a length of data given two strings to find in order"""
    try:
        names = get_key_data(data,"name")
    except:
        raise ValueError("No se han podido obtener los nombres")
    try:
        find_first_string= find_string_in_name(first_string,names,first_string_times)
    except:
        raise ValueError("No se ha ejecutado correctamente la función find_string_in_name con el primer string")
    try:
        find_second_string = find_string_in_name(second_string,find_first_string,second_string_times)
        return len(find_second_string)
    except:
        raise ValueError("No se ha ejecutado correctamente la función find_string_in_name con el segundo string ")

    

def count_species(list_group_url: list):
    """this function combine the pokemon species from a pokemon, remove duplicates and return total quantity of species """

    egg_groups_data=[]
    try:
        for egg_group_url in list_group_url:
            egg_groups_lists= get_pokemon_species_from_group(get_api_data(egg_group_url))
            for specie in egg_groups_lists:
                egg_groups_data.append(specie)
        
        return len(set(egg_groups_data))
    except:
        raise ValueError("Ha ocurrido un error al usar la función count_species()")

def species_to_procreate(specie_endpoint: str):
    """this function return quantity of species can be couple with raichu"""
    try:
        data_specie = get_api_data(specie_endpoint)
    except:
        raise ValueError("No se ha podido obtener los datos del endpoint de especie en la función species_to_procreate()")
    
    try:
        egg_groups_url = get_egg_group_url(data_specie)
    except:
        raise ValueError("No se ha podido obtener la url del egg group en la función get_egg_group() al ejecutarla en species_to_procreate()")
    try:
        quantity_species_procreate= count_species(egg_groups_url)
        return quantity_species_procreate
    except:
        raise ValueError("No se ha podido contar el total de especies para procrear con el egg group dado")

    

