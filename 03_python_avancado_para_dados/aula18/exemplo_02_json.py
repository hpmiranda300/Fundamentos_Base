import requests
import json
from pathlib import Path

from pydantic import BaseModel, ConfigDict

class PokemonSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # <-- Configuração V2

    name: str
    type: str        


def pegar_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    caminho_arquivo = Path(__file__).parent / f"{data['name']}.json"
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'], type=types)

pokemon = pegar_pokemon(15)
print(pokemon)
pokemon = pegar_pokemon(24)
print(pokemon)