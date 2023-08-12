from pydantic import BaseModel


class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    phone: str


class MyInfoResponse(BaseModel):
    user: User
    timestamp: int
