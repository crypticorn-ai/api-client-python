from enum import Enum
from typing import Union, List
from pydantic import BaseModel


# Define Service-Specific Scopes
class HiveScope(Enum):
    MODEL_READ = "hive:model:read"
    MODEL_WRITE = "hive:model:write"
    DATA_READ = "hive:data:read"
    DATA_WRITE = "hive:data:write"


class TradeScope(Enum):
    TRADE_READ = "trade:read"
    TRADE_WRITE = "trade:write"
    BOTS_READ = "trade:bots:read"
    BOTS_WRITE = "trade:bots:write"
    API_KEYS_READ = "trade:api_keys:read"
    API_KEYS_WRITE = "trade:api_keys:write"
    ORDERS_READ = "trade:orders:read"
    ORDERS_WRITE = "trade:orders:write"
    ACTIONS_EXECUTE = "trade:actions:execute"


# Centralized API Scope Management
class APIScope(BaseModel):
    allowed_scopes: List[Union[HiveScope, TradeScope]]

    def has_access(self, scope: Union[HiveScope, TradeScope]) -> bool:
        return scope in self.allowed_scopes


# Example Usage:
user_scope = APIScope(allowed_scopes=[HiveScope.MODEL_READ, TradeScope.TRADE_WRITE])

# Check Access
print(user_scope.has_access(HiveScope.MODEL_READ))  # True
print(user_scope.has_access(TradeScope.ORDERS_READ))  # False
