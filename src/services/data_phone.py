from repositories.repository import AbstractRepository, RedisRepository
from typing import Union
from schemas.data_phone import CreateDataPhone
from exceptions import KeyAlreadyExists, KeyNotFound


class DataPhoneService:

    def __init__(self, repository: Union[AbstractRepository, RedisRepository]):
        self.repository = repository

    async def get(self, phone: str):

        if result := self.repository.get_one(key=f"phone_{phone}"):
            return result
        raise KeyNotFound

    async def add(self, data_phone: CreateDataPhone):

        if await self.get(data_phone.phone):
            raise KeyAlreadyExists

        return await self.repository.add_one(key=f"phone_{data_phone.phone}", data=data_phone)

    async def update(self, data_phone: CreateDataPhone):

        if not await self.get(data_phone.phone):
            return await self.repository.add_one(key=f"phone_{data_phone.phone}", data=data_phone)

        raise KeyNotFound