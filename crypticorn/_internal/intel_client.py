"""Lightweight shared base for Intel service clients (news, sentiment, social, defi, derivatives).

These services don't use OpenAPI-generated code. Instead they provide a thin
async/sync HTTP layer that is wire-compatible with the existing ``client.py``
infrastructure (shared ``aiohttp.ClientSession``, ``configure()``, ``close()``).
"""

from __future__ import annotations

import json
import ssl
from typing import Any, Optional
from urllib.parse import urlencode

import aiohttp
from asgiref.sync import async_to_sync


class IntelConfiguration:
    """Minimal configuration matching the interface expected by ``BaseAsyncClient``."""

    def __init__(
        self,
        host: str = "",
        access_token: Optional[str] = None,
        api_key: Optional[dict[str, str]] = None,
    ) -> None:
        self.host = host.rstrip("/")
        self.access_token = access_token
        self.api_key = api_key


class _IntelRestClient:
    """Thin HTTP helper that reuses an external ``aiohttp.ClientSession`` when provided."""

    def __init__(self, configuration: IntelConfiguration) -> None:
        self.configuration = configuration
        self.pool_manager: Optional[aiohttp.ClientSession] = None
        self.is_sync: bool = False

    def _build_headers(self) -> dict[str, str]:
        headers: dict[str, str] = {"Content-Type": "application/json"}
        if self.configuration.access_token:
            headers["Authorization"] = f"Bearer {self.configuration.access_token}"
        if self.configuration.api_key:
            api_key_value = self.configuration.api_key.get("APIKeyHeader")
            if api_key_value:
                headers["X-API-Key"] = api_key_value
        return headers

    async def request(
        self,
        method: str,
        url: str,
        *,
        timeout: float = 300,
    ) -> Any:
        headers = self._build_headers()
        should_close = False
        session = self.pool_manager

        if session is None:
            session = aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(
                    limit=100,
                    ssl=ssl.create_default_context(),
                ),
                trust_env=True,
            )
            should_close = self.is_sync

        try:
            async with session.request(method, url, headers=headers, timeout=aiohttp.ClientTimeout(total=timeout)) as resp:
                data = await resp.read()
                if resp.status >= 400:
                    raise aiohttp.ClientResponseError(
                        request_info=resp.request_info,
                        history=resp.history,
                        status=resp.status,
                        message=data.decode("utf-8", errors="replace"),
                        headers=resp.headers,
                    )
                return json.loads(data) if data else None
        finally:
            if should_close and session is not None:
                await session.close()

    async def close(self) -> None:
        pass


class IntelBaseClient:
    """Base class for all Intel service clients.

    Subclasses define API methods as ``async def _<name>(...) -> Any`` and
    expose public wrappers that automatically handle sync/async dispatch.
    """

    config_class = IntelConfiguration

    def __init__(
        self,
        config: IntelConfiguration,
        http_client: Optional[aiohttp.ClientSession] = None,
        is_sync: bool = False,
    ) -> None:
        self.config = config
        self._is_sync = is_sync
        self.base_client = _IntelRestClient(configuration=config)
        self.base_client.is_sync = is_sync
        if http_client is not None:
            self.base_client.pool_manager = http_client

    def _url(self, path: str) -> str:
        return f"{self.config.host}/{path.lstrip('/')}"

    @staticmethod
    def _build_query(params: dict[str, Any]) -> str:
        filtered = {k: str(v) for k, v in params.items() if v is not None and v != ""}
        if isinstance(filtered.get("only_verified"), str):
            filtered["only_verified"] = filtered["only_verified"].lower()
        return f"?{urlencode(filtered)}" if filtered else ""

    async def _get(self, path: str, params: Optional[dict[str, Any]] = None) -> Any:
        qs = self._build_query(params or {})
        return await self.base_client.request("GET", f"{self._url(path)}{qs}")

    def _sync_wrap(self, coro: Any) -> Any:
        return async_to_sync(coro)
