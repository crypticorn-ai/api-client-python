from crypticorn.auth.client.exceptions import UnauthorizedException
from crypticorn.auth import CreateApiKeyRequest
from crypticorn.common import BaseUrl, Scope
from crypticorn.common import MarketType
from crypticorn.hive import Configuration as HiveConfig
from crypticorn.pay import ProductModel
from crypticorn import ApiClient
from crypticorn.trade import ExchangeKeyModel
import asyncio
from crypticorn.trade import BotModel, BotStatus
from datetime import datetime, timedelta

jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoiNE81UFhZTElBbmtveFRBQ3BRY2UiLCJpYXQiOjE3NDQ0OTE5NTksImV4cCI6MTc0NDQ5NTU1OSwic2NvcGVzIjpbInJlYWQ6cHJlZGljdGlvbnMiXX0.ycS7KK-5BhXHpiqR_NVJWQDu6pdygYi4YsV1IT11TFc"


async def main():
    async with ApiClient(base_url=BaseUrl.LOCAL, api_key="") as client:
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
        # res = await client.trade.bots.create_bot(
        #     BotModel(
        #         name="test",
        #         strategy_id="123",
        #         api_key_id="123",
        #         allocation=100,
        #         status=BotStatus.RUNNING,
        #     )
        # )
        # try:
        #     res = await client.auth.login.create_api_key(
        #         CreateApiKeyRequest(
        #             name="writes products",
        #             scopes=[Scope.READ_METRICS_EXCHANGES],
        #             expires_at=datetime.now() + timedelta(days=30),
        #         )
        #     )
        #     print(res.api_key)
        #     # ress = await client.auth.login.get_api_keys()
        #     # print(ress)
        #     # res = await client.auth.login.verify_api_key('asdf')
        #     # print(res)

        # except UnauthorizedException as e:
        #     print(e.body)
        res = await client.metrics.exchanges.get_available_exchanges(
            market=MarketType.FUTURES, symbol="BTC"
        )
        print(res)
        # res = await client.trade.bots.get_bots()
        # print(res)
        # res = await client.auth.login.verify_api_key(api_key='sk6SGlb8rxWZr744FV4zTmDLr5w5Gs')
        # print(res)


async def new_client():
    async with ApiClient(base_url=BaseUrl.DEV) as client:
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
