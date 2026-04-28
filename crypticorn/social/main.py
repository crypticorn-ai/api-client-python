from __future__ import annotations

from typing import Any, Awaitable, Optional, Union

from crypticorn._internal.intel_client import IntelBaseClient


class SocialClient(IntelBaseClient):
    """Client for the Crypticorn Social API (``/v1/social``)."""

    def get_posts(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        asset: Optional[str] = None,
        source: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "from": from_,
            "to": to,
            "asset": asset,
            "source": source,
            "limit": limit,
            "cursor": cursor,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("posts", params))
        return self._get("posts", params)

    def get_metrics(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        asset: Optional[str] = None,
        source: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "from": from_,
            "to": to,
            "asset": asset,
            "source": source,
            "limit": limit,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("metrics", params))
        return self._get("metrics", params)

    def get_trending(
        self,
        *,
        window_hours: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {"window_hours": window_hours, "limit": limit}
        if self._is_sync:
            return self._sync_wrap(self._get("trending", params))
        return self._get("trending", params)
