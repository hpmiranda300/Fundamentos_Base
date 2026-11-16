#from pydantic import BaseModel
#class PokemonSchema(BaseModel):
#    name: str
#    type: str
#
#    class Config:
#        orm_mode = True

from pydantic import BaseModel, ConfigDict

class PokemonSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # <-- Configuração V2

    name: str
    type: str  