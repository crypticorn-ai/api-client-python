# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from crypticorn.dex.client.api.signals_api import SignalsApi
    from crypticorn.dex.client.api.status_api import StatusApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from crypticorn.dex.client.api.signals_api import SignalsApi
from crypticorn.dex.client.api.status_api import StatusApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
