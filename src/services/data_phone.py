from repositories.repository import AbstractRepository, RedisRepository
from typing import Union
from schemas.data_phone import CreateDataPhone, CheckDataPhone
from exceptions import KeyAlreadyExists, KeyNotFound
from config import logger
import json


class DataPhoneService:

    def __init__(self, repository: Union[AbstractRepository, RedisRepository]):
        self.repository = repository

    async def get(self, data_phone: CheckDataPhone):

        if result := await self.repository.get_one(key=f"phone_{data_phone.phone}"):
            return result
        raise KeyNotFound

    async def add(self, data_phone: CreateDataPhone):

        try:
            if await self.repository.get_one(key=f"phone_{data_phone.phone}"):
                raise KeyAlreadyExists
            await self.repository.add_one(key=f"phone_{data_phone.phone}", data=data_phone)

        except KeyNotFound:
            if await self.repository.add_one(key=f"phone_{data_phone.phone}", data=data_phone):
                return data_phone
            raise BaseException

    async def update(self, data_phone: CreateDataPhone):

        if await self.repository.get_one(key=f"phone_{data_phone.phone}"):
            return await self.repository.add_one(key=f"phone_{data_phone.phone}", data=data_phone)

        raise KeyNotFound