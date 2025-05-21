from crypticorn.auth.client.exceptions import UnauthorizedException
from crypticorn.auth import CreateApiKeyRequest
from crypticorn.common import BaseUrl, Scope, Service, MarketType, InternalExchange
from crypticorn.hive import Configuration as HiveConfig, DataInfo, ModelCreate
from crypticorn.hive import Coins, Target
from crypticorn.pay import ProductUpdate, ProductCreate
from crypticorn import ApiClient
from crypticorn.trade import (
    ExchangeKey,
    Configuration as TradeConfig,
    FuturesTradingActionCreate,
    TradingActionType,
)
import asyncio
from crypticorn.trade import Bot, BotStatus
from crypticorn.klines import Timeframe
from datetime import datetime, timedelta
import time

jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYlowNUVqS2ZqWGpXdDBTMDdvOSIsImF1ZCI6ImFwcC5jcnlwdGljb3JuLmNvbSIsImlzcyI6ImFjY291bnRzLmNyeXB0aWNvcm4uY29tIiwianRpIjoiUm1RcE9BZWNaV0t1djNDemNjd1YiLCJpYXQiOjE3NDQ1NDU1NTQsImV4cCI6MTc0NDU0OTE1NCwic2NvcGVzIjpbInJlYWQ6cHJlZGljdGlvbnMiXX0.UVD4-6Z5C6yYAaL6LMDwbGJCrhpk7TkDNo1TbinvDzM"


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
        #     Bot(
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
        # res = await client.auth.user.user_by_id(id="123")
        # print(res)
        # res = await client.pay.products.update_product(
        #     id="67fba7640d89242bbaf3d4a5",
        #     product_update=ProductUpdate(
        #         # name="test2",
        #         # description="test",
        #         # price=100,
        #         # duration=30,
        #         # scopes=[Scope.READ_PAY_NOW, Scope.WRITE_PAY_PRODUCTS],
        #         # is_active=True,
        #     ),
        # )
        # print(res)
        # assert res.scopes == [Scope.READ_PAY_NOW, Scope.WRITE_PAY_PRODUCTS]
        # res = await client.pay.products.get_products()
        # print([print(p.name) for p in res])
        # res = await client.auth.login.get_api_keys()
        # print(res)
        # res = await client.metrics.exchanges.get_exchange_mappings_without_preload_content(
        #     market="spot", exchange="lol"
        # )
        # print(await res.json())
        # res = await client.klines.funding.get_funding_rates_fmt(
        #     symbol="BTC-USDT",
        # )
        # print(res)
        # res = await client.auth.login.verify()
        # print(res)
        # model = await client.hive.models.create_model(
        #     ModelCreate(
        #         name="test_187",
        #         coin_id=Coins.ENUM_1,
        #         target=Target.TATOOINE,
        #     )
        # )
        # await client.hive.data.download_data(
        #     version="1.0",
        #     model_id=model.id,
        #     feature_size="small",
        # )
        # from crypticorn.common import Service
        # client.configure(config=HiveConfig(host="http://localhost:8000"), service=Service.HIVE)
        # res = await client.hive.status.ping()
        # print(res)
        # res = await client.metrics.exchanges.get_exchange_mappings(
        #     exchange="binance", market=MarketType.FUTURES
        # )
        # print(res.data)
        # result = await client.metrics.exchanges.get_exchange_mappings(
        #     market=MarketType.FUTURES
        # )
        # exchanges = set([r.exchange_name for r in result])
        # print(exchanges)
        # res = await client.klines.ohlcv.get_ohlcv_data_fmt(
        #     symbol="BTCUSDT",
        #     timeframe=Timeframe.ENUM_1D,
        #     market=MarketType.FUTURES,
        #     limit=100,
        # )
        # print(res)
        # res = await client.metrics.tokens.get_stable_tokens()
        # print(res)
        # res = await client.metrics.marketcap.get_marketcap_symbols_fmt()
        # print(res)
        res = await client.trade.orders.get_orders()
        print(res)


async def configure_client():
    async with ApiClient(base_url=BaseUrl.DEV) as client:
        client.configure(
            config=HiveConfig(host="http://localhost:8000"), service=Service.HIVE
        )
        res = await client.hive.status.ping()
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(configure_client())
    # response = asyncio.run(client.hive.models.get_all_models())
    # print(response)
    # asyncio.run(client.close())
    # asyncio.run(client.close())
