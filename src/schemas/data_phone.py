from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber


class CreateDataPhone(BaseModel):
    phone: PhoneNumber
    address: str
