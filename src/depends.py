from db.base import redis_client
from fastapi import Depends
from repositories.repository import RedisRepository, PhoneDataRepository

from services import data_phone


def get_phone_data_repository(
) -> PhoneDataRepository:
    return PhoneDataRepository(redis_client)


def get_phone_data_service(
    repository: PhoneDataRepository = Depends(get_phone_data_repository),
):
    return data_phone.DataPhoneService(repository)