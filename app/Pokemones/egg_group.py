
def get_egg_group_url(specie_data: dict):
    """This function get egg groups url from give specie and return a list with egg_groups"""
    if specie_data is not None or specie_data != "":
        egg_group = [egg_group["url"] for egg_group in specie_data["egg_groups"] ]
        return egg_group
    else:
        raise ValueError("No se ha proporcionado el argumento 'specie_data' para ejecutar correctamente la función get_egg_group_url()")

def get_egg_group_name(specie_data: dict):
    """This function get egg groups name from give specie and return a list with egg_groups"""

    egg_group = [egg_group["name"] for egg_group in specie_data["egg_groups"] ]

    return egg_group

def get_pokemon_species_from_group(egg_group_data: dict):
    """this function return a list with pokemon species from a egg group"""

    pokemon_specie = [specie["name"] for specie in egg_group_data["pokemon_species"] ]

    return pokemon_specie





