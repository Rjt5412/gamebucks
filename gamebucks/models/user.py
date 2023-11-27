from pydantic import BaseModel
from gamebucks.models.game import GameHours


class Address(BaseModel):
    id: str
    house_no: str
    street: str
    city: str
    country: str
    zipcode: str
    
class CreateUser(BaseModel):
    name: str
    contact: str
    email: str
    addresses: list[Address]
    default_address_id: str
    hashed_pass: str
    stats: list[GameHours]


