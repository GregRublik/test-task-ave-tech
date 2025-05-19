import pytest


@pytest.mark.asyncio
async def test_write_data(async_client):
    response = await async_client.post(
        "/write_data",
        json={
            "phone": "+79536767195",
            "address": "string",
        },
    )
    print(response.json())
    assert response.status_code in (200, 409)


# @pytest.mark.asyncio
# async def test_check_data(async_client):
#
#     response = await async_client.get(
#         "/check_data",
#         params={
#             "phone": "+79536767195",
#         },
#     )
#     print(response.json())
#     assert response.status_code == 200
#
#     response = await async_client.get(
#         "/check_data",
#         params={
#             "phone": "879536767195",
#         },
#     )
#     print(response.json())
#     assert response.status_code == 422


@pytest.mark.asyncio
async def test_update_data(async_client):
    response = await async_client.put(
        "/update_data",
        json={
            "phone": "+79536767195",
            "address": "string",
        },
    )
    print(response.json())
    assert response.status_code == 200
