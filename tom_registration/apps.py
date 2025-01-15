from django.apps import AppConfig
from django.urls import path, include


class TomRegistrationConfig(AppConfig):
    name = 'tom_registration'

    def include_url_paths(self):
        """
        Integration point for adding URL patterns to the Tom Common URL configuration.
        This method should return a list of URL patterns to be included in the main URL configuration.
        """
        urlpatterns = [
            path('register/', include('tom_registration.urls', namespace='registration'))
        ]
        return urlpatterns
