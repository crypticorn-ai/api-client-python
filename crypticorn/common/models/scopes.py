from enum import Enum


class APIScope:

    class Hive(str, Enum):
        MODEL_READ = "hive:model:read"
        DATA_READ = "hive:data:read"
        MODEL_WRITE = "hive:model:write"
        DATA_WRITE = "hive:data:write"

    class Trade(str, Enum):
        BOTS_READ = "trade:bots:read"
        API_KEYS_READ = "trade:api_keys:read"
        ORDERS_READ = "trade:orders:read"
        ACTIONS_READ = "trade:actions:read"
        BOTS_WRITE = "trade:bots:write"
        API_KEYS_WRITE = "trade:api_keys:write"
        ORDERS_WRITE = "trade:orders:write"
        ACTIONS_WRITE = "trade:actions:write"

print(APIScope.Trade.BOTS_READ.value)
