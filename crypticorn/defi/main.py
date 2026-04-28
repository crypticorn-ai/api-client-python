from __future__ import annotations

from typing import Any, Awaitable, Optional, Union

from crypticorn._internal.intel_client import IntelBaseClient


class DefiClient(IntelBaseClient):
    """Client for the Crypticorn DeFi API (``/v1/defi``)."""

    def get_protocols(
        self,
        *,
        chain: Optional[str] = None,
        category: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "chain": chain,
            "category": category,
            "from": from_,
            "to": to,
            "limit": limit,
            "cursor": cursor,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("protocols", params))
        return self._get("protocols", params)

    def get_yields(
        self,
        *,
        chain: Optional[str] = None,
        asset: Optional[str] = None,
        min_apy: Optional[float] = None,
        max_apy: Optional[float] = None,
        limit: Optional[int] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "chain": chain,
            "asset": asset,
            "min_apy": min_apy,
            "max_apy": max_apy,
            "limit": limit,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("yields", params))
        return self._get("yields", params)

    def get_chain(
        self,
        chain: str,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        if self._is_sync:
            return self._sync_wrap(self._get(f"chains/{chain}"))
        return self._get(f"chains/{chain}")
