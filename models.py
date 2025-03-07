from enum import Enum
from typing import List, Optional, Annotated, Dict
from pydantic import BaseModel, Field, model_validator

class Exchange(str, Enum):
    '''Supported exchanges'''
    KUCOIN = "kucoin"
    BINGX = "bingx"

class FuturesBalance(BaseModel):
    '''Model for futures balance'''
    apiKeyId: str = Field(..., description="API key ID")
    asset: str = Field(..., description="Asset/Currency code")
    balance: float = Field(..., description="Total balance/equity")
    available: float = Field(..., description="Available balance for trading/withdrawal")
    unrealizedPnl: float = Field(..., description="Unrealized profit and loss")
    usedMargin: Optional[float] = Field(None, description="Used/Position margin")
    frozenAmount: Optional[float] = Field(None, description="Frozen/Hold funds")
    
class FuturesBalanceError(BaseModel):
    # TODO: may be removed in the future when dealing with /futures/balance endpoint
    '''Model for futures balance error response'''
    apiKeyId: str = Field(..., description="API key ID")
    error: str = Field(..., description="Error message")

class SpotBalance(BaseModel):
    '''Model for spot balance'''
    apiKeyId: str = Field(..., description="API key ID")
    asset: str = Field(..., description="Asset/Currency code")
    balance: float = Field(..., description="Total balance/equity")
    available: float = Field(..., description="Available balance for trading/withdrawal")

class MarketType(str, Enum):
    '''Type of market'''
    spot = "spot"
    futures = "futures"

class TradingActionType(str, Enum):
    '''Type of trading action'''
    open_long = "open_long" # Open a long position
    open_short = "open_short" # Open a short position
    close_long = "close_long" # Close a long position
    close_short = "close_short" # Close a short position 
    
class OrderStatus(str, Enum):
    '''Status of the order'''
    new = "new" # order has been placed but not yet processed (e.g., limit TP/SL orders)
    filled = "filled" # order has been filled
    partially_filled = "partially_filled" # order has been partially filled (only temporary as the order will be filled completely unless of a black swan price drop)
    cancelled = "cancelled" # order has been cancelled prior to being filled e.g. all TPs are filled and SLs are marked as cancelled, action has expired, could not change leverage (bingx) etc.
    failed = "failed" # order failed to be placed due to an error (e.g., insufficient balance) or HTTP errors

class TPSL(BaseModel):
    '''Model for take profit and stop loss targets'''
    price_delta: Optional[Annotated[float, Field(..., ge=0)]] = Field(None, description="The price delta to calculate the limit price from the current market price, e.g. for a SL of 1% the it would be 0.99")
    price: Optional[float] = Field(None, description="The limit price to set the target at. If not set, the limit price will be calculated from the current market price.")
    execution_id: Optional[str] = Field(None, description="Execution ID of the order. Will be added by the system")
    allocation: Annotated[float, Field(..., ge=0, le=1)] = Field(..., description="Percentage of the order to sell")

    @model_validator(mode="after")
    def validate_fields(cls, values: 'TPSL'):
        if values.price_delta is None and values.price is None:
            raise ValueError("Either percentage or price must be set")
        return values

class MarginMode(str, Enum):
    '''Margin mode for futures trades'''
    isolated = "isolated"
    cross = "cross"

class SymbolInfo(BaseModel):
    '''Model for symbol info'''
    symbol: str = Field(..., description="Symbol")
    precision_price: str = Field(..., description="Price precision")
    precision_size: str = Field(..., description="Quantity precision")
    max_size: Optional[str] = Field(None, description="Maximum order size")
    min_size: Optional[str] = Field(None, description="Minimum order size")
    max_long_leverage: Optional[int] = Field(None, description="Maximum leverage for long positions")
    max_short_leverage: Optional[int] = Field(None, description="Maximum leverage for short positions")

class ExchangeInfo(BaseModel):
    '''Model for exchange info'''
    symbol: str = Field(..., description="Symbol")
    market_price: float = Field(..., description="Market price")
    symbol_info: SymbolInfo = Field(..., description="Symbol info")
    
class SpotTradingAction(BaseModel):
    '''Model for spot trading actions'''
    id: Optional[str] = Field(None, description="Placeholder for the id of the trading action. Will be added by the system, therefore optional.")
    execution_id: Optional[str] = Field(None, description="UID for the execution of the order. Leave empty for open actions. Required on close actions if you havent't placed a TP/SL before. A specific TP/SL execution ID of the opening order.")
    open_order_execution_id: Optional[str] = Field(None, description="UID for the order to close. Leave empty for open actions. Required on close actions. The main execution ID of the opening order.")
    action_type: TradingActionType = Field(..., description="The type of action.")
    market_type: MarketType = Field(..., description="The type of market the action is for.")
    strategy_id: str = Field(..., description="UID for the strategy.")
    client_timestamp: int = Field(..., description="Timestamp of when the action was created on the client side.")
    symbol: str = Field(..., description="Trading symbol or asset pair in format: 'symbol/quote_currency' (see market service for valid symbols)")
    is_limit: Optional[bool] = Field(False, description="Whether this is a limit order.")
    limit_price: Optional[float] = Field(None, description="The limit price for limit orders. If not set, the market price will be used.")
    allocation: Annotated[float, Field(gt=0, le=1)] = Field(None, description="How much of bot's balance to use for the order (for open actions). How much of the position to close (for close actions). 0=0%, 1=100%.")
    take_profit: Optional[List[TPSL]] = Field(None, description="Take profit targets. Can be set for open actions only. Multiple can be set.")
    stop_loss: Optional[List[TPSL]] = Field(None, description="Stop loss values. Can be set for open actions only. Multiple can be set.")
    expiry_timestamp: Optional[int] = Field(None, description="Timestamp of when the order will expire. If not set, the order will not expire. Applied on each bot individually.")

    @model_validator(mode="after")
    def validate_fields(cls, values: 'SpotTradingAction'):
        if not isinstance(values.action_type, TradingActionType):
            raise ValueError("Invalid action_type. Must be of type TradingActionType")
        if not isinstance(values.market_type, MarketType):
            raise ValueError("Invalid market_type. Must be of type MarketType")
        if values.open_order_execution_id is None and values.action_type in [TradingActionType.close_short, TradingActionType.close_long]:
            raise ValueError("open_order_execution_id must be set for close actions")
        if (values.take_profit or values.stop_loss) and values.action_type in [TradingActionType.close_long, TradingActionType.close_short]:
            raise ValueError("take_profit and stop_loss can only be set for open actions")
        return values

class FuturesTradingAction(SpotTradingAction):
    '''Model for futures trading actions'''
    leverage: Optional[Annotated[int, Field(1, ge=1)]] = Field(description="Leverage to use for futures trades.")
    margin_mode: Optional[MarginMode] = Field(MarginMode.isolated, description="Margin mode for futures trades.")
    
    @model_validator(mode="after")
    def validate_fields(cls, values: 'FuturesTradingAction'):
        values = super().validate_fields(values)
        if values.market_type == MarketType.futures and values.leverage is None:
            raise ValueError("leverage must be set for futures trades")
        if not isinstance(values.margin_mode, MarginMode):
            raise ValueError("Invalid margin_mode. Must be of type MarginMode")
        return values
    
class OrderInfo(BaseModel):
    '''Model for order information. For more details use 'OrderModel' from db.models'''
    order_id: str = Field(..., description="UID for the order in the exchange")

class ApiErrorType(str, Enum):
    '''Type of API error'''
    USER_ERROR = "user error"
    """user error by people using the bot on the dashboard frontend"""
    EXCHANGE_ERROR = "exchange error"
    """re-tryable error by the exchange or network conditions"""
    SERVER_ERROR = "server error"
    """server error that needs a new version rollout for a fix"""
    NO_ERROR = "no error"
    '''error that does not need to be handled or does not affect the program or is a placeholder.'''

class ApiErrorIdentifier(str, Enum):
    '''API error identifiers'''
    SUCCESS = "success"
    UNAUTHORIZED = "invalid_api_key"
    INVALID_SIGNATURE = "invalid_signature"
    INVALID_TIMESTAMP = "invalid_timestamp"
    IP_RESTRICTED = "ip_address_is_not_authorized"
    PERMISSION_DENIED = "insufficient_permissions_spot_and_futures_required"
    USER_FROZEN = "user_account_is_frozen"
    RATE_LIMIT = "rate_limit_exceeded"
    INVALID_PARAMETER = "invalid_parameter_provided"
    REQUEST_SCOPE_EXCEEDED = "request_scope_limit_exceeded"
    CONTENT_TYPE_ERROR = "invalid_content_type"
    URL_NOT_FOUND = "requested_resource_not_found"
    ORDER_NOT_FOUND = "order_does_not_exist"
    ORDER_ALREADY_FILLED = "order_is_already_filled"
    ORDER_IN_PROCESS = "order_is_being_processed"
    ORDER_LIMIT_EXCEEDED = "order_quantity_limit_exceeded"
    ORDER_PRICE_INVALID = "order_price_is_invalid"
    POST_ONLY_REJECTED = "post_only_order_would_immediately_match"
    
    POSITION_NOT_FOUND = "position_does_not_exist"  
    POSITION_LIMIT_EXCEEDED = "position_limit_exceeded"
    NO_POSITION_TO_CLOSE = "no_position_available_to_close"
    POSITION_SUSPENDED = "position_opening_temporarily_suspended"
    INSUFFICIENT_BALANCE = "insufficient_balance"
    INSUFFICIENT_MARGIN = "insufficient_margin"
    
    LEVERAGE_EXCEEDED = "leverage_limit_exceeded"
    RISK_LIMIT_EXCEEDED = "risk_limit_exceeded"
    LIQUIDATION_PRICE_VIOLATION = "order_violates_liquidation_price_constraints"
    INVALID_MARGIN_MODE = "invalid_margin_mode"
    
    SYSTEM_ERROR = "internal_system_error"
    SYSTEM_CONFIG_ERROR = "system_configuration_error"
    SERVICE_UNAVAILABLE = "service_temporarily_unavailable"
    SYSTEM_BUSY = "system_is_busy_please_try_again_later"
    MAINTENANCE = "system_under_maintenance"
    RPC_TIMEOUT = "rpc_timeout"
    SETTLEMENT_IN_PROGRESS = "system_settlement_in_process"
    
    TRADING_SUSPENDED = "trading_is_suspended"
    TRADING_LOCKED = "trading_has_been_locked"
    
    UNKNOWN_ERROR = "unknown_error_occurred"
    HTTP_ERROR = "http_request_error"
    BLACK_SWAN = "black_swan"
    
    ACTION_EXPIRED = "trading_action_expired"
    BOT_DISABLED = "bot_disabled"
    NEW_TRADING_ACTION = "new_trading_action"
    ORDER_SIZE_TOO_SMALL = "order_size_too_small"
    ORDER_SIZE_TOO_LARGE = "order_size_too_large"


class ApiError(Enum):
    '''API error codes'''
    # Success
    SUCCESS = (ApiErrorIdentifier.SUCCESS, ApiErrorType.NO_ERROR)
    # Authentication/Authorization
    UNAUTHORIZED = (ApiErrorIdentifier.UNAUTHORIZED, ApiErrorType.SERVER_ERROR)
    INVALID_SIGNATURE = (ApiErrorIdentifier.INVALID_SIGNATURE, ApiErrorType.SERVER_ERROR) 
    INVALID_TIMESTAMP = (ApiErrorIdentifier.INVALID_TIMESTAMP, ApiErrorType.SERVER_ERROR)
    IP_RESTRICTED = (ApiErrorIdentifier.IP_RESTRICTED, ApiErrorType.SERVER_ERROR)
    PERMISSION_DENIED = (ApiErrorIdentifier.PERMISSION_DENIED, ApiErrorType.USER_ERROR)
    USER_FROZEN = (ApiErrorIdentifier.USER_FROZEN, ApiErrorType.USER_ERROR)
    
    # Rate Limiting
    RATE_LIMIT = (ApiErrorIdentifier.RATE_LIMIT, ApiErrorType.EXCHANGE_ERROR)
    
    # Invalid Parameters
    INVALID_PARAMETER = (ApiErrorIdentifier.INVALID_PARAMETER, ApiErrorType.SERVER_ERROR)
    REQUEST_SCOPE_EXCEEDED = (ApiErrorIdentifier.REQUEST_SCOPE_EXCEEDED, ApiErrorType.EXCHANGE_ERROR)
    CONTENT_TYPE_ERROR = (ApiErrorIdentifier.CONTENT_TYPE_ERROR, ApiErrorType.SERVER_ERROR)
    URL_NOT_FOUND = (ApiErrorIdentifier.URL_NOT_FOUND, ApiErrorType.SERVER_ERROR)
    
    # Order Related
    ORDER_NOT_FOUND = (ApiErrorIdentifier.ORDER_NOT_FOUND, ApiErrorType.SERVER_ERROR)
    ORDER_ALREADY_FILLED = (ApiErrorIdentifier.ORDER_ALREADY_FILLED, ApiErrorType.SERVER_ERROR)
    ORDER_IN_PROCESS = (ApiErrorIdentifier.ORDER_IN_PROCESS, ApiErrorType.NO_ERROR)
    ORDER_LIMIT_EXCEEDED = (ApiErrorIdentifier.ORDER_LIMIT_EXCEEDED, ApiErrorType.USER_ERROR)
    ORDER_PRICE_INVALID = (ApiErrorIdentifier.ORDER_PRICE_INVALID, ApiErrorType.SERVER_ERROR)
    POST_ONLY_REJECTED = (ApiErrorIdentifier.POST_ONLY_REJECTED, ApiErrorType.SERVER_ERROR)
    BLACK_SWAN = (ApiErrorIdentifier.BLACK_SWAN, ApiErrorType.USER_ERROR)
    #CONTRA_ORDER_MISSING = "No contra order available"
    
    # Position Related
    POSITION_NOT_FOUND = (ApiErrorIdentifier.POSITION_NOT_FOUND, ApiErrorType.USER_ERROR)
    POSITION_LIMIT_EXCEEDED = (ApiErrorIdentifier.POSITION_LIMIT_EXCEEDED, ApiErrorType.USER_ERROR)
    NO_POSITION_TO_CLOSE = (ApiErrorIdentifier.NO_POSITION_TO_CLOSE, ApiErrorType.USER_ERROR)
    POSITION_SUSPENDED = (ApiErrorIdentifier.POSITION_SUSPENDED, ApiErrorType.EXCHANGE_ERROR)
    #FUTURES_BRAWL_RESTRICTED = "Operation restricted for Futures Brawl", ApiErrorType.USER_ERROR
    
    # Balance/Margin
    INSUFFICIENT_BALANCE = (ApiErrorIdentifier.INSUFFICIENT_BALANCE, ApiErrorType.USER_ERROR)
    INSUFFICIENT_MARGIN = (ApiErrorIdentifier.INSUFFICIENT_MARGIN, ApiErrorType.USER_ERROR)
    
    # Leverage/Risk
    LEVERAGE_EXCEEDED = (ApiErrorIdentifier.LEVERAGE_EXCEEDED, ApiErrorType.SERVER_ERROR)
    RISK_LIMIT_EXCEEDED = (ApiErrorIdentifier.RISK_LIMIT_EXCEEDED, ApiErrorType.SERVER_ERROR)
    LIQUIDATION_PRICE_VIOLATION = (ApiErrorIdentifier.LIQUIDATION_PRICE_VIOLATION, ApiErrorType.SERVER_ERROR)
    INVALID_MARGIN_MODE = (ApiErrorIdentifier.INVALID_MARGIN_MODE, ApiErrorType.SERVER_ERROR)
    
    # System Status
    SYSTEM_ERROR = (ApiErrorIdentifier.SYSTEM_ERROR, ApiErrorType.EXCHANGE_ERROR)
    SYSTEM_CONFIG_ERROR = (ApiErrorIdentifier.SYSTEM_CONFIG_ERROR, ApiErrorType.EXCHANGE_ERROR)
    SERVICE_UNAVAILABLE = (ApiErrorIdentifier.SERVICE_UNAVAILABLE, ApiErrorType.EXCHANGE_ERROR)
    SYSTEM_BUSY = (ApiErrorIdentifier.SYSTEM_BUSY, ApiErrorType.EXCHANGE_ERROR)
    MAINTENANCE = (ApiErrorIdentifier.MAINTENANCE, ApiErrorType.EXCHANGE_ERROR)
    RPC_TIMEOUT = (ApiErrorIdentifier.RPC_TIMEOUT, ApiErrorType.EXCHANGE_ERROR)
    SETTLEMENT_IN_PROGRESS = (ApiErrorIdentifier.SETTLEMENT_IN_PROGRESS, ApiErrorType.EXCHANGE_ERROR)
    
    # Trading Status
    TRADING_SUSPENDED = (ApiErrorIdentifier.TRADING_SUSPENDED, ApiErrorType.EXCHANGE_ERROR)
    TRADING_LOCKED = (ApiErrorIdentifier.TRADING_LOCKED, ApiErrorType.EXCHANGE_ERROR)
    
    # Generic
    UNKNOWN_ERROR = (ApiErrorIdentifier.UNKNOWN_ERROR, ApiErrorType.EXCHANGE_ERROR)
    HTTP_ERROR = (ApiErrorIdentifier.HTTP_ERROR, ApiErrorType.EXCHANGE_ERROR)

    # Our Errors
    ACTION_EXPIRED = (ApiErrorIdentifier.ACTION_EXPIRED, ApiErrorType.NO_ERROR)
    BOT_DISABLED = (ApiErrorIdentifier.BOT_DISABLED, ApiErrorType.USER_ERROR)
    NEW_TRADING_ACTION = (ApiErrorIdentifier.NEW_TRADING_ACTION, ApiErrorType.NO_ERROR)
    ORDER_SIZE_TOO_SMALL = (ApiErrorIdentifier.ORDER_SIZE_TOO_SMALL, ApiErrorType.USER_ERROR)
    ORDER_SIZE_TOO_LARGE = (ApiErrorIdentifier.ORDER_SIZE_TOO_LARGE, ApiErrorType.USER_ERROR)

    @property
    def identifier(self) -> str:
        return self.value[0]

    @property
    def type(self) -> ApiErrorType:
        return self.value[1]

class ErrorResponse(BaseModel):
    '''Model for error response'''
    error: ApiError

    @property
    def value(self):
        return (self.error.identifier, self.error.type)