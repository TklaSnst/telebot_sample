from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    pass


class UserAddSchema(BaseSchema):
    tg_id: int | None
    username: str = Field(max_length=100)


class UserGetSchema(BaseSchema):
    id: str
    tg_id: int | None
    username: str = Field(max_length=100)
    is_active: bool


class ItemAddSchema(BaseSchema):
    name: str = Field(max_length=100)
    dsc: str = Field(max_length=1000)
    price: int | None
