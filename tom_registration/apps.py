from django.apps import AppConfig
from django.urls import path, include
from django.conf import settings


class TomRegistrationConfig(AppConfig):
    name = 'tom_registration'

    def include_url_paths(self):
        """
        Integration point for adding URL patterns to the Tom Common URL configuration.
        This method should return a list of URL patterns to be included in the main URL configuration.
        """
        registration_strategy = settings.TOM_REGISTRATION['REGISTRATION_STRATEGY']
        urlpatterns = [
            path('', include(f'tom_registration.registration_flows.{registration_strategy}.urls',
                             namespace='registration')),
        ]
        return urlpatterns

    def nav_items(self):
        """
        Integration point for adding items to the navbar.
        This method should return a list of partial templates to be included in the navbar.
        """
        return ['tom_registration/partials/register_button.html']
