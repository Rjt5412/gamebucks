from pydantic import BaseModel

class Category(BaseModel):
    id: str
    name: str
    description: str

class GameTag(BaseModel):
    id: str
    name: str

class CreateGame(BaseModel):
    title: str
    name: str
    description: str
    price: float
    image_url: str | None
    categories: list[Category] | None
    tags: list[GameTag] | None
    quantity: int


class UpdateGame(BaseModel):
    id: str
    title: str
    name: str
    description: str
    price: float
    image_url: str | None
    categories: list[Category]
    quantity: int


class GameHours(BaseModel):
    game_id: str
    hours: float