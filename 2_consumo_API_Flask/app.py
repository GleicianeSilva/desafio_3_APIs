'''

1. Criar uma nova rota para listar as localizações. A rota deverá ser acessível através do caminho /locations. A página deverá ser renderizada através do template locations html. A página deverá conter uma tabela com as seguintes informações: nome, tipo e dimensão. A tabela deverá conter um link para a página de perfil da localização.

2. Criar uma nova rota para listar os episódios. A rota deverá ser acessível através do caminho /episodes. A página deverá ser renderizada através do template episodes.html. A página deverá conter uma tabela com as seguintes informações: nome, data de lançamento e código. A tabela deverá conter um link para a página de perfil do episódio.

3. Criar uma nova rota para exibir o perfil da localização. A rota deverá ser acessível através do caminho /location/<id>. A página deverá ser renderizada através do template location.html. A página deverá conter as seguintes informações: nome, tipo, dimensão e uma lista com os personagens que aparecem na localização. A lista deverá conter um link para a página de perfil do personagem.

4. Criar uma nova rota para exibir o perfil do episódio. A rota deverá ser acessível através do caminho /episode/<id>. A página deverá ser renderizada através do template episode.html. A página deverá conter as seguintes informações: nome, data de lançamento, código e uma lista com os personagens que aparecem no episódio. A lista deverá conter um link para a página de perfil do personagem.

5. Na página de perfil do personagem, adicione as seguintes informações: espécie, gênero, origem e localização. As informações de origem, localização e episódios em que o personagem aparece devem conter um link para a página de perfil da localização.

'''

from flask import Flask, render_template

import urllib.request, json

app = Flask(__name__)

@app.route("/")

def get_list_characters_page():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])



@app.route("/profile/<id>")

def get_profile(id):

    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    episodes = []

    for episode_url in dict["episode"]:
        episode_response = urllib.request.urlopen(episode_url)
        episode_data = episode_response.read()
        episode_dict = json.loads(episode_data)
        episodes.append(episode_dict)

    return render_template("profile.html", profile=dict, episodes=episodes)



@app.route("/lista")

def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "Nome": character["name"],
            "Status": character["status"]
        }
        characters.append(character)

    return {"characters": characters}



@app.route("/locations")

def get_list_locations():

    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    locations = response.read()
    dict = json.loads(locations)

    locations = []

    for location in dict["results"]:
        location = {
            "Nome": location["name"],
            "Tipo": location["type"],
            "Dimensao": location["dimension"]
        }
        locations.append(location)

    return {"locations": locations}



@app.route("/location/<id>")
def get_location(id):

    url = "https://rickandmortyapi.com/api/location" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    location = json.loads(data)

    # character_ids = [int(char.split("/")[-1]) for char in location["residents"]]
    characters = []

    # for char_id in character_ids:
    for character in location["residents"]:
        character_url = f"https://rickandmortyapi.com/api/character/{character}"
        character_response = urllib.request.urlopen(character_url)
        character_data = character_response.read()
        character_dict = json.loads(character_data)
        characters.append(character_dict)

    return render_template("location.html", location=location, characters=characters)



@app.route("/episodes")

def get_list_episodes():

    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)

    episodes = []

    for episode in dict["results"]:
        episode = {
            "Nome": episode["name"],
            "Data de Lancamento": episode["air_date"],
            "Episodio": episode["episode"]
        }
        episodes.append(episode)

    return {"episodes": episodes}



@app.route("/episode/<id>")
def get_episode(id):

    url = "https://rickandmortyapi.com/api/episode" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    episode = json.loads(data)

    #character_ids = [int(char.split("/")[-1]) for char in episode["residents"]]
    characters = []

    # for char_id in character_ids:
    for character in episode["residents"]:
        character_url = f"https://rickandmortyapi.com/api/character/{character}"
        character_response = urllib.request.urlopen(character_url)
        character_data = character_response.read()
        character_dict = json.loads(character_data)
        characters.append(character_dict)

    return render_template("episode.html", episode=episode, characters=characters)