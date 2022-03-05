import requests
from api_vars import API_URL

def get_api_data(api_url: list):
    """
    api_url: receive the api's url withouth endopint
    endpoint: receive the endpoint to complement api_url 
    this function use the get method for obtain data of an endpoint and return a json response"""
    
    try:
        response = requests.get(api_url)
        data_json = response.json()
        
        return data_json
    except:
        raise ValueError("Hay un problema con la url ingresada en la función get_api_data()")

def get_specie_endpoint(specie: str):
    """this function return the endpoint from a given specie"""
    if specie is None or specie != "":
        data= get_api_data(API_URL+'pokemon/'+specie)
        return data["species"]["url"]
    else:
        raise TypeError("El argumento especie no ha sido dado en la función get_specie_endpoint()") 
    



