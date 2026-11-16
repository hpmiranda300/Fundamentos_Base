import requests
#from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict  # <-- Importe ConfigDict

#pydantic_core._pydantic_core.ValidationError: 1 validation error for PokemonSchema name
#Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='beedrill', input_type=str]
#For further information visit https://errors.pydantic.dev/2.14/v/int_parsing

#class PokemonSchema(BaseModel):
#    #name: int
#    name: str
#    type: str
#
#    class Config:
#        orm_mode = True



#Essa configuração serve para que o Pydantic consiga ler atributos de objetos ORM 
# (como SQLAlchemy/SQLModel). Com from_attributes = True, o aviso sumirá completamente ao rodar o 
# script.
class PokemonSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # <-- Configuração V2

    name: str
    type: str        

def pegar_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    #print(data)
    data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'], type=types)

pokemon = pegar_pokemon(15)
print(pokemon)