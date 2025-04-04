from typing import Optional
from typing_extensions import Annotated, Doc
from crypticorn.common import (
    AuthScheme,
    HTTPBearer,
    APIKeyHeader,
    Service,
    Domain,
    HTTPMethod,
)


class AuthClient:
    """
    Middleware for verifying API requests. Verifies the validity of the authentication token, allowed scopes, etc.
    """

    def __init__(
        self,
        service: Annotated[Service, Doc("The service that is using the client.")],
        auth_schemes: Annotated[
            Optional[list[AuthScheme]],
            Doc(
                "The authentication schemes to use for the client. Defaults to HTTPBearer and APIKeyHeader. Can be overridden per request."
            ),
        ] = [HTTPBearer, APIKeyHeader],
        whitelist: Annotated[
            Optional[list[Domain]],
            Doc("The domains that are allowed full access to the service."),
        ] = [Domain.PROD, Domain.DEV],
        excluded_methods: Annotated[
            Optional[list[HTTPMethod]], Doc("The methods that are excluded by default.")
        ] = [],
    ):
        self.auth_schemes = auth_schemes
        self.service = service
        self.whitelist = whitelist
        self.excluded_methods = excluded_methods

    def auth(self) -> bool:
        raise NotImplementedError()
