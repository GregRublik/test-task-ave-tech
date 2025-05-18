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
        return await data_phone_service.get(data_phone)
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
        return await data_phone_service.add(data_phone)
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
    try:

        return await data_phone_service.update(data_phone)
    except KeyNotFound as e:
        print("key not found")
        raise HTTPException(
            status_code=e.status_code,
            detail={"success": False, "message": "this number not found"},
        )