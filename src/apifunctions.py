import os
import requests
from dotenv import load_dotenv
from functools import reduce
import operator

def foursquare(latitude, longitude, category, radius):
    
    client_id = os.getenv("tok1")
    client_secret = os.getenv("tok2")
    parametros = {
        "client_id": client_id,
        "client_secret": client_secret,
        "ll": f"{latitude}, {longitude}",
        #"query": "cafe",
        'radius': radius,
        "v": "20180323",
        'categoryId':category
    }
    url_query = 'https://api.foursquare.com/v2/venues/search'
    url_recomendados = 'https://api.foursquare.com/v2/venues/explore'

    resp = requests.get(url_query, params = parametros).json()

    return resp['response']['venues']

def foursquarequery(latitude, longitude, kueri, radius):
    
    client_id = os.getenv("tok1")
    client_secret = os.getenv("tok2")
    parametros = {
        "client_id": client_id,
        "client_secret": client_secret,
        "ll": f"{latitude}, {longitude}",
        "query": kueri,
        'radius': radius,
        "v": "20180323"
    }
    url_query = 'https://api.foursquare.com/v2/venues/search'
    url_recomendados = 'https://api.foursquare.com/v2/venues/explore'

    resp = requests.get(url_query, params = parametros).json()

    return resp['response']['venues']

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def type_point(lista):
    return {"type":"Point", "coordinates": lista}

def extraetodo(json):
    todo = {"nombre": ["name"], "latitud": ["location", "lat"], "longitud": ["location", "lng"], 'category':['categories', 0 ,'name'], 'distance': ['location', 'distance']}
    total = []
    for elemento in json:
        libre = {key: getFromDict(elemento, value) for key,value in todo.items()}
        libre["location"] = type_point([libre["latitud"], libre["longitud"]])
        total.append(libre)
    return total