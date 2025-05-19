from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic_extra_types.phone_numbers import PhoneNumber

from exceptions import KeyAlreadyExists, KeyNotFound
from schemas.data_phone import CreateDataPhone, CheckDataPhone

from services.data_phone import DataPhoneService
from depends import get_phone_data_service
router = APIRouter(tags=["DATA PHONE"])


@router.get("/check_data",)
async def check_data(
    data_phone: Annotated[CheckDataPhone, Query()],
    data_phone_service: Annotated[DataPhoneService, Depends(get_phone_data_service)]
):
    try:
        data = await data_phone_service.get(data_phone)
        return {"detail": {"success": True, 'data_phone': data}}
    except KeyNotFound as e:
        raise HTTPException(
            status_code=e.status_code,
            detail={"success": False, "message": "this number not found"},
        )

@router.post("/write_data",)
async def check_data(
    data_phone: CreateDataPhone,
    data_phone_service: Annotated[DataPhoneService, Depends(get_phone_data_service)]
):
    try:
        await data_phone_service.add(data_phone)
        return {"detail": {"success": True, 'write_data_phone': data_phone.model_dump()}}
    except KeyAlreadyExists as e:
        raise HTTPException(
            status_code=e.status_code,
            detail={"success": False, "message": "this number already exists"},
        )


@router.put("/update_data",)
async def update_data(
    data_phone: CreateDataPhone,
    data_phone_service: Annotated[DataPhoneService, Depends(get_phone_data_service)]
):
    """
    решил что лучше добавить отдельный метод для изменения данных по номеру
    """

    try:

        await data_phone_service.update(data_phone)
        return {"detail": {"success": True, 'updated_data_phone': data_phone.model_dump()}}
    except KeyNotFound as e:
        raise HTTPException(
            status_code=e.status_code,
            detail={"success": False, "message": "this number not found"},
        )