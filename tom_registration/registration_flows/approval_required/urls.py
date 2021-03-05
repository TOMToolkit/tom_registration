from django.contrib.auth.views import LoginView
from django.urls import include, path

from .forms import CustomAuthenticationForm
from .views import ApprovalRegistrationView, UserApprovalView

app_name = 'tom_registration'


urlpatterns = [
    path('accounts/login/', LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('accounts/register/', ApprovalRegistrationView.as_view(), name='register'),
    path('accounts/approve/<int:pk>/', UserApprovalView.as_view(), name='approve')
]