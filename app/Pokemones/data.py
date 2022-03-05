import requests
from api_vars import API_URL

def get_api_data(api_url):
    """
    api_url: receive the api's url withouth endopint
    endpoint: receive the endpoint to complement api_url 
    this function use the get method for obtain data of an endpoint and return a json response"""

    response = requests.get(api_url)
    data_json = response.json()

    return data_json

def get_specie_endpoint(specie):
    """this function return the endpoint from a given specie"""
    data= get_api_data(API_URL+'pokemon/'+specie)

    return data["species"]["url"]



