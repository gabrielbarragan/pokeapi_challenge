# pokeapi_challenge
Este repositorio contiene el desarrollo de algunas funciones para interactuar con la **PokéAPI** (https://pokeapi.co/). 

### Versión de Python y librerías:

Python 3.9.7.

En el archivo “requirements.txt” se encuentran las versiones de las librerías que se usaron para el desarrollo de este proyecto, de igual forma se relacionarán a continuación:

certifi==2021.10.8

charset-normalizer==2.0.12

idna==3.3

requests==2.27.1

urllib3==1.26.8

### El módulo Pokemones:

En el módulo **Pokemones** se encuentran todas las funciones desarrolladas. A continuación se describen los archivos sus funciones y uso:

### **data.py:**

En este se encuentran las funciones `get_api_data()` y `get_especie_endpoint()`

`get_api_data()`: recibe un endpoint y retorna los datos en formato json

`get_especie_endpoint()`: recibe un string con el nombre de un pokemon y retorna un endpoint con el endpoint de la especie.

### **counters.py:**

En este se encuentran las funciones `count_names()`, `count_species()` y `species_to_procreate()`.

`count_names()`: Evalúa la existencia de 2 strings en los nombres obtenidos al consultar un endpoint cualquiera que contenga la llave “name”, cuenta la cantidad de nombres que cumplen con las condiciones que se le indiquen.

`count_species()`: Recibe una lista de urls de los “egg groups” de un pokemon y obtiene sin duplicados la cantidad de especies que pertenecen a los “egg groups” retorna un entero.

`species_to_procreate()`: Recibe el endpoint de una especie, consulta las urls de los egg groups y retorna la cantidad de especies que pueden procrear con la especie indicada.

### egg_group.py:

En este se encuentran las funciones `get_egg_group_url()`, `get_egg_group_name()` y `get_pokemon_species_from_group()` necesarias para poder realizar el segundo punto del reto. 

`get_egg_group_url()`: Recibe la data recolectada de un endpoint de especie y retorna una lista con las urls de los “egg groups” de la especie dada. 

`get_egg_group_name()`: Recibe la data recolectada de un endpoint de especie y retorna una lista con los nombres de los “egg groups” de la especie dada. 

`get_pokemon_species_from_group()`: Recibe los datos de un endpoint de egg group y retorna una lista con los nombres de las especies que pertenecen al grupo dado.

### find_string_in_data.py:

En este se encuentran las funciones `get_key_data()` y `find_string_in_name()`.

`get_key_data()`: Recibe la data de un endpoint que contenga la llave “results” y busca la llave (”key”) dada dentro de la data ingresada, devuelve una lista con los valores dentro de la llave solicitada. En este caso esta función se usó para obtener los nombres dentro de la data recibida con el endpoint donde se consultaron todos los pokemon.

`find_string_in_name()`: Busca un substring que se encuentra una cantidad de veces dada dentro de cada uno los nombres dados en una lista, retorna una lista con los nombres que cumplen con la condición. en este caso se usa para buscar cada una de las cadenas de texto dentro de los nombres de los pokemon.

### type.py:

En este se encuentran las funciones `get_ids_smaller()` y `get_weights_in_pokemon_of_type()` necesarias para realizar el punto 3 del reto.

`get_ids_smaller()`: Esta función recibe la data del endpoint “type”, la clave en esta data que contiene las urls de los pokemones con id y el máximo id que se quiere obtener, retorna los id que son menores al max_id dado.

`get_weights_in_pokemon_of_type()`:Esta función recibe un tipo de pokemon en string y el máximo id que se quiere obtener, retorna una lista con el peso máximo y mínimo de los pokemones de un tipo específico que no superan el número de id requerido. 

### api_vars.py:

contiene la url de la API y el endpoint para consultar todos los pokemon.

### main.py:

En este archivo se hace uso de todas las funciones para resolver cada uno de los puntos del reto.
