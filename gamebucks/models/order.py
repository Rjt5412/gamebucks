from pydantic import BaseModel
from gamebucks.models.user import Address

class OrderItem(BaseModel):
    game_id: str
    quantity: int

class Order(BaseModel):
    user_id: str
    games: list[OrderItem]
    total: float
    billingAddress: Address
    status: str

class Cart(BaseModel):
    games: list[OrderItem]