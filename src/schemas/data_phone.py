from pydantic import BaseModel, model_validator
from pydantic_extra_types.phone_numbers import PhoneNumber


class CheckDataPhone(BaseModel):
    phone: PhoneNumber

    @model_validator(mode="after")
    def remove_prefix_from_phone(self) -> "CheckDataPhone":
        if self.phone:
            self.phone = self.phone.removeprefix("tel:+").replace("-", "")
        return self


class CreateDataPhone(CheckDataPhone):
    address: str
