from abc import ABC, abstractmethod
from redis.asyncio.client import Redis

from schemas.data_phone import CreateDataPhone


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
        return await self.client.set(key, data)

    async def get_one(self, key: str):
        return await self.client.get(key)


class PhoneDataRepository(RedisRepository):

    async def add_one(self, key: str, data: CreateDataPhone):
        """
        :param key:
        :param data: возможно стоило просто сохранять key: phone, value: address, но я сделал так
        :return:
        """

        return await self.client.set(key, str(data.model_dump()))

