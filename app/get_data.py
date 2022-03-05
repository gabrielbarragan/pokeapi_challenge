import requests


def get_api_data(api_url, endpoint):
    """
    api_url: receive the api's url withouth endopint
    endpoint: receive the endpoint to complement api_url 
    this function use the get method for obtain data of an endpoint and return a json response"""

    ENDPOINT_COMPLETE = api_url + endpoint
    response = requests.get(ENDPOINT_COMPLETE)
    data_json = response.json()

    return data_json



