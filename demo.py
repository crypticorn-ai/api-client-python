from crypticorn import ApiClient
import asyncio

async def main():
    jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoidFNtS3BSMVd4VmIxM2sxbXlZVVgiLCJpYXQiOjE3NDM0NTU0MTgsImV4cCI6MTc0MzQ1OTAxOCwic2NvcGVzIjpbInJlYWQ6cHJlZGljdGlvbnMiXX0.AcnoW3uLpQPu1m05S4m-EFYR7hHr_CiuYq_qlwRITzk"

    client = ApiClient(base_url="http://localhost", jwt=jwt)
    # json response - NOT WORKING
    response = await client.pay.products.get_products_without_preload_content()
    print(10 * "=" + "This is the raw json response" + 10 * "=")
    print(response.json())

    # serialized response with pydantic models
    response = await client.pay.products.get_products()
    print(10 * "=" + "This is the serialized response with pydantic models" + 10 * "=")
    print(response)

    # json response with http info
    response = await client.pay.products.get_products_with_http_info()
    print(10 * "=" + "This is the json response with http info" + 10 * "=")
    print(response)

    response = await client.auth.admin.user_list()
    print(10 * "=" + "This is the user list" + 10 * "=")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())

