from crypticorn.auth import AuthClient, AddWalletRequest
from crypticorn.auth.client.exceptions import UnauthorizedException
from crypticorn.common import BaseURL, ApiVersion
from crypticorn import ApiClient
import asyncio

jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoiT0NsVUc2dG9ORWJYNkM1alpQZUUiLCJpYXQiOjE3NDM4ODkxNDIsImV4cCI6MTc0Mzg5Mjc0Miwic2NvcGVzIjpbInJlYWQ6cHJlZGljdGlvbnMiXX0.ej1O5cRni-pHczAMUR6JvP9VyTCb-e4J847zUYs6luw"

async def main():
    async with ApiClient(base_url=BaseURL.LOCAL, jwt=jwt) as client:
        # json response
        # response = await client.pay.products.get_products_without_preload_content()
        # print(10 * "=" + "This is the raw json response" + 10 * "=")
        # print(await response.json())

        # # serialized response with pydantic models
        # response = await client.pay.products.get_products()
        # print(
        #     10 * "=" + "This is the serialized response with pydantic models" + 10 * "="
        # )
        # print(response)

        # # json response with http info
        # response = await client.pay.products.get_products_with_http_info()
        # print(10 * "=" + "This is the json response with http info" + 10 * "=")
        # print(response)

        # response = await client.auth.admin.user_list_with_http_info()
        # print(response)

        # response = await client.hive.models.get_all_models()
        # print(response)

        # res = await client.login.verify(jwt)
        # print(res)

        response = await client.trade.bots.get_bots()
        print(response)


async def auth():
    async with AuthClient(
        base_url=BaseURL.LOCAL, api_version=ApiVersion.V1, jwt=jwt
    ) as client:
        try:
            res = await client.login.verify()
            print(res.sub)
        except UnauthorizedException as e:
            print(e.body)


if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(auth())
    # client = ApiClient(base_url="http://localhost", api_key="1234567890")
    # response = asyncio.run(client.hive.models.get_all_models())
    # print(response)
    # asyncio.run(client.close())
