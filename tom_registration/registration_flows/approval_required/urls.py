from django.contrib.auth.views import LoginView
from django.urls import include, path

from .views import ApprovalRegistrationView, CustomLoginView, UserApprovalView

app_name = 'tom_registration'


urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/register/', ApprovalRegistrationView.as_view(), name='register'),
    path('accounts/approve/<int:pk>/', UserApprovalView.as_view(), name='approve')
]