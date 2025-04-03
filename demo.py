from crypticorn import ApiClient
from crypticorn.hive import ModelCreate, Coins, Target
import asyncio

jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoiUHZMRlI3RU9SUEZoeTdyRzg0SWMiLCJpYXQiOjE3NDM1MzU0NTksImV4cCI6MTc0MzUzOTA1OSwic2NvcGVzIjpbInJlYWQ6cHJlZGljdGlvbnMiXX0.91rIX0uQ76U_sv9F0rdahRUDa7MKqOPL_aMH88-EAhg"


async def main():
    async with ApiClient(base_url="http://localhost", jwt=jwt) as client:
        # json response
        response = await client.pay.products.get_products_without_preload_content()
        print(10 * "=" + "This is the raw json response" + 10 * "=")
        print(await response.json())

        # serialized response with pydantic models
        response = await client.pay.products.get_products()
        print(10 * "=" + "This is the serialized response with pydantic models" + 10 * "=")
        print(response)

        # json response with http info
        response = await client.pay.products.get_products_with_http_info()
        print(10 * "=" + "This is the json response with http info" + 10 * "=")
        print(response)

        # response = await client.auth.admin.user_list_with_http_info()
        # print(response)

        # response = await client.hive.models.get_all_models()
        # print(response)



if __name__ == "__main__":
    # asyncio.run(main())
    client = ApiClient(base_url="http://localhost", api_key="1234567890")
    response = asyncio.run(client.hive.models.get_all_models())
    print(response)
    asyncio.run(client.close())
