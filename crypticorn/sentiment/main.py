from __future__ import annotations

from typing import Any, Awaitable, Optional, Union

from crypticorn._internal.intel_client import IntelBaseClient


class SentimentClient(IntelBaseClient):
    """Client for the Crypticorn Sentiment API (``/v1/sentiment``)."""

    def get_asset_sentiment(
        self,
        asset: str,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {"from": from_, "to": to, "limit": limit}
        if self._is_sync:
            return self._sync_wrap(self._get(f"assets/{asset}", params))
        return self._get(f"assets/{asset}", params)

    def get_article_sentiment(
        self,
        article_id: str,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        if self._is_sync:
            return self._sync_wrap(self._get(f"articles/{article_id}"))
        return self._get(f"articles/{article_id}")

    def get_signals(
        self,
        *,
        min_confidence: Optional[float] = None,
        min_articles: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Union[dict[str, Any], Awaitable[dict[str, Any]]]:
        params = {
            "min_confidence": min_confidence,
            "min_articles": min_articles,
            "limit": limit,
        }
        if self._is_sync:
            return self._sync_wrap(self._get("signals", params))
        return self._get("signals", params)
