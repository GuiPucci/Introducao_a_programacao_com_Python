import requests

# def retorna_dados_cep(cep):
# response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
# print(response.status_code)
# print(response.text)
# print(type(response.text))
# print(response.json)
# print(type(response.json))
# dados_cep = response.json()
# print(dados_cep["logradouro"])
# return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # response = retorna_response("https://web.dio.me/home")
    # print(response)
    # retorna_dados_cep("19064557")
    dados_pokemon = retorna_dados_pokemon("charmander")

    print(dados_pokemon["sprites"]["front_shiny"])

    print(f"Name: {dados_pokemon['name']}")
    print(f"Height: {dados_pokemon['height']}")
    print(f"Weight: {dados_pokemon['weight']}")
    print(f"Base Experience: {dados_pokemon['base_experience']}")

    print("Types:")
    for type_info in dados_pokemon['types']:
        print(f"- {type_info['type']['name']}")

    print("Abilities:")
    for ability_info in dados_pokemon['abilities']:
        print(f"- {ability_info['ability']['name']}")
