from __future__ import annotations

from typing import Any, Awaitable, Optional, Union

from crypticorn._internal.intel_client import IntelBaseClient


class NewsClient(IntelBaseClient):
    """Client for the Crypticorn News API (``/v1/news``)."""

    def get_articles(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        asset: Optional[str] = None,
        source: Optional[str] = None,
        category: Optional[str] = None,
        lang: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "from": from_,
            "to": to,
            "asset": asset,
            "source": source,
            "category": category,
            "lang": lang,
            "limit": limit,
            "cursor": cursor,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("articles", params))
        return self._get("articles", params)

    def search(
        self,
        q: str,
        *,
        mode: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        asset: Optional[str] = None,
        source: Optional[str] = None,
        category: Optional[str] = None,
        lang: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "q": q,
            "mode": mode,
            "from": from_,
            "to": to,
            "asset": asset,
            "source": source,
            "category": category,
            "lang": lang,
            "limit": limit,
            "cursor": cursor,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("search", params))
        return self._get("search", params)

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

    def get_sources(self) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        if self._is_sync:
            return self._sync_wrap(self._get("sources"))
        return self._get("sources")
