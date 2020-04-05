import requests

character = requests.get('https://rickandmortyapi.com/api/character').json()
episode = requests.get('https://rickandmortyapi.com/api/episode').json()
location = requests.get('https://rickandmortyapi.com/api/location').json()



    
def lista_episodios():
    episode = requests.get('https://rickandmortyapi.com/api/episode').json()
    info_e = episode["info"]

    l_episodios = []
    for i in range(info_e["pages"]):
        string = "https://rickandmortyapi.com/api/episode?page="
        string += str(i+1)
        episodios = requests.get(string).json()
        l_episodios += episodios["results"]

    return l_episodios

def info_episodio(numero):
    string = 'https://rickandmortyapi.com/api/episode/'
    string += str(numero)
    episodio = requests.get(string).json()
    return episodio

def info_personaje(numero):
    string = 'https://rickandmortyapi.com/api/character/'
    string += str(numero)
    personaje = requests.get(string).json()
    return personaje

def info_lugar(numero):
    string = 'https://rickandmortyapi.com/api/location/'
    string += str(numero)
    lugar = requests.get(string).json()
    return lugar


def lista_personajes():
    characters = requests.get('https://rickandmortyapi.com/api/character').json()
    info_c = characters["info"]

    l_characters = []
    for i in range(info_c["pages"]):
        string = "https://rickandmortyapi.com/api/character?page="
        string += str(i+1)
        character = requests.get(string).json()
        l_characters += character["results"]
    
    return l_characters

def nombre_personaje(link):
    nombre = {}
    personaje = requests.get(link).json()
    nombre["nombre"] = personaje["name"]
    nombre["id"] = personaje["id"]
    return nombre




