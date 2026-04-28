from __future__ import annotations

from typing import Any, Awaitable, Optional, Union

from crypticorn._internal.intel_client import IntelBaseClient


class DerivativesClient(IntelBaseClient):
    """Client for the Crypticorn Derivatives API (``/v1/derivatives``)."""

    def get_funding_rates_latest(
        self,
        *,
        asset: Optional[str] = None,
        exchange: Optional[str] = None,
        min_abs_rate: Optional[float] = None,
        stale_after_minutes: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "asset": asset,
            "exchange": exchange,
            "min_abs_rate": min_abs_rate,
            "stale_after_minutes": stale_after_minutes,
            "limit": limit,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("funding-rates/latest", params))
        return self._get("funding-rates/latest", params)

    def get_funding_rates_history(
        self,
        *,
        asset: Optional[str] = None,
        exchange: Optional[str] = None,
        venue_symbol: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "asset": asset,
            "exchange": exchange,
            "venue_symbol": venue_symbol,
            "from": from_,
            "to": to,
            "limit": limit,
            "cursor": cursor,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("funding-rates/history", params))
        return self._get("funding-rates/history", params)

    def get_funding_intervals(
        self,
        *,
        asset: Optional[str] = None,
        exchange: Optional[str] = None,
        only_verified: Optional[bool] = None,
        limit: Optional[int] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "asset": asset,
            "exchange": exchange,
            "only_verified": only_verified,
            "limit": limit,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("funding-intervals", params))
        return self._get("funding-intervals", params)

    def get_funding_opportunities(
        self,
        *,
        asset: Optional[str] = None,
        exchange: Optional[str] = None,
        settlement_type: Optional[str] = None,
        min_net_profit: Optional[float] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "asset": asset,
            "exchange": exchange,
            "settlement_type": settlement_type,
            "min_net_profit": min_net_profit,
            "from": from_,
            "to": to,
            "limit": limit,
            "cursor": cursor,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("funding-opportunities", params))
        return self._get("funding-opportunities", params)

    def get_exchanges_status(
        self,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        if self._is_sync:
            return self._sync_wrap(self._get("exchanges/status"))
        return self._get("exchanges/status")
