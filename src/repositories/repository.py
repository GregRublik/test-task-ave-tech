from abc import ABC, abstractmethod
from redis.asyncio.client import Redis

from schemas.data_phone import CreateDataPhone
from config import logger


class AbstractRepository(ABC):
    """
    Абстрактный репозиторий нужен чтобы при наследовании определяли его базовые методы работы с бд
    """
    client = None

    @abstractmethod
    async def add_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_list(self, *args, **kwargs):
        raise NotImplementedError


class RedisRepository:
    """
    Репозиторий для работы с Redis
    """

    def __init__(self, client: Redis):
        self.client = client

    async def add_one(self, key: str, data: str):
        res = await self.client.set(key, data)
        return res

    async def get_one(self, key: str):
        res = await self.client.get(key)
        return res


class PhoneDataRepository(RedisRepository):

    async def add_one(self, key: str, data: CreateDataPhone):
        """
        :param key:
        :param data: возможно стоило просто сохранять key: phone, value: address, но я сделал так
        :return:
        """
        res = await self.client.set(key, str(data.model_dump()))
        return res

