import warnings
import logging
from crypticorn.common.logging import configure_logging

warnings.filterwarnings("default", "", DeprecationWarning)
configure_logging()
logging.captureWarnings(True)
# TODO: remove logging in next major release

from crypticorn.client import AsyncClient, SyncClient, ApiClient

__all__ = ["AsyncClient", "SyncClient", "ApiClient"]
