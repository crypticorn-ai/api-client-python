from crypticorn.common import BaseUrl
from crypticorn.hive import Configuration as HiveConfig
from crypticorn.pay import ProductModel
from crypticorn import ApiClient
import dotenv
import asyncio
from crypticorn.metrics import Market
from crypticorn.trade import BotModel, BotStatus

dotenv.load_dotenv()
jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoiZUxVVDJ6QzFnV3A2UDcwTjdVM3UiLCJpYXQiOjE3NDQyMDI3ODEsImV4cCI6MTc0NDIwNjM4MSwic2NvcGVzIjpbInJlYWQ6aGl2ZTptb2RlbCIsInJlYWQ6aGl2ZTpkYXRhIiwicmVhZDp0cmFkZTpib3RzIiwicmVhZDp0cmFkZTpvcmRlcnMiLCJyZWFkOnRyYWRlOmFjdGlvbnMiLCJyZWFkOnRyYWRlOnN0cmF0ZWdpZXMiLCJyZWFkOnRyYWRlOmV4Y2hhbmdlcyIsInJlYWQ6dHJhZGU6ZnV0dXJlcyIsInJlYWQ6dHJhZGU6bm90aWZpY2F0aW9ucyIsInJlYWQ6dHJhZGU6YXBpX2tleXMiLCJyZWFkOnBheTpub3ciLCJyZWFkOnBheTpwcm9kdWN0cyIsInJlYWQ6cGF5OnBheW1lbnRzIiwid3JpdGU6aGl2ZTptb2RlbCIsIndyaXRlOnRyYWRlOmJvdHMiLCJ3cml0ZTp0cmFkZTpmdXR1cmVzIiwid3JpdGU6dHJhZGU6bm90aWZpY2F0aW9ucyIsIndyaXRlOnRyYWRlOmFwaV9rZXlzIiwid3JpdGU6dHJhZGU6c3RyYXRlZ2llcyIsInJlYWQ6cHJlZGljdGlvbnMiLCJ3cml0ZTpwYXk6cHJvZHVjdHMiLCJ3cml0ZTpwYXk6bm93IiwicmVhZDpwcmVkaWN0aW9ucyJdfQ.Pr6kX_Sfi2dU_PT2JEfWEb5Lu3eVIX6mdlvTENEu1l0"


async def main():
    async with ApiClient(base_url="http://localhost", jwt=jwt) as client:
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

        # response = await client.auth.login.get_api_keys()
        # print(response)

        # # response = await client.hive.models.get_all_models()
        # # print(response)

        # res = await client.auth.login.verify()
        # print(res)

        # response = await client.trade.bots.get_bots()
        # print(response)
        # await client.pay.products.update_product(
        #     id="123",
        #     product_model=ProductModel(
        #         name="test",
        #         description="test",
        #     ),
        # )

        # res = await client.pay.products.get_products()
        # print(res)

        # res = await client.metrics.status.health_check()
        # print(res)
        # res = await client.metrics.marketcap.get_marketcap_symbols_fmt(
        #     market=Market.FUTURES,
        #     exchange="binance",
        # )
        # print(res)
        # res = await client.metrics.tokens.get_tokens_fmt(token_type="wrappes")
        res = await client.trade.bots.create_bot(
            BotModel(
                name="test",
                strategy_id="123",
                api_key_id="123",
                allocation=100,
                status=BotStatus.RUNNING,
            )
        )
        # try:
        #     res = await client.auth.login.create_api_key(
        #         CreateApiKeyRequest(
        #             name="writes products",
        #             scopes=[Scope.WRITE_PAY_PRODUCTS],
        #             expiresIn=60 * 60 * 24 * 30,  # 30 days
        #         )
        #     )
        #     print(res.api_key)
        #     res = await client.auth.login.get_api_keys()
        #     print(res)
        #     latest = res[-1].id
        #     await client.auth.login.delete_api_key_with_http_info(latest)
        #     res = await client.auth.login.get_api_keys()
        #     print(res)
        # except UnauthorizedException as e:
        #     print(e.body)


async def new_client():
    async with ApiClient(base_url=BaseUrl.DEV, jwt=jwt) as client:
        client.configure(
            config=HiveConfig(host="http://localhost:8000"), sub_client=client.hive
        )
        res = await client.pay.products.get_products_with_http_info()
        print(res.data)


if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(new_client())
    # client = ApiClient(base_url="http://localhost", api_key="1234567890")
    # response = asyncio.run(client.hive.models.get_all_models())
    # print(response)
    # asyncio.run(client.close())
