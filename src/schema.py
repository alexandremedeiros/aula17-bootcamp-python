#schema de dados, view da API
from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True