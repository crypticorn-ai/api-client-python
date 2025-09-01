# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from crypticorn.notification.client.api.notifications_api import NotificationsApi
    from crypticorn.notification.client.api.settings_api import SettingsApi
    from crypticorn.notification.client.api.status_api import StatusApi
    from crypticorn.notification.client.api.templates_api import TemplatesApi

else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from crypticorn.notification.client.api.notifications_api import NotificationsApi
from crypticorn.notification.client.api.settings_api import SettingsApi
from crypticorn.notification.client.api.status_api import StatusApi
from crypticorn.notification.client.api.templates_api import TemplatesApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
