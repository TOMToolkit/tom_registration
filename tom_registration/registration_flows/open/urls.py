from django.urls import path

from tom_registration.registration_flows.open.views import OpenRegistrationView

app_name = 'tom_registration'


urlpatterns = [
    path('register/', OpenRegistrationView.as_view(), name='register'),
]