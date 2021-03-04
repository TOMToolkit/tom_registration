from django.urls import path

from tom_registration.views import ApprovalRegistrationView, OpenRegistrationView, UserApprovalView

app_name = 'tom_registration'


urlpatterns = [
    path('register/open/', OpenRegistrationView.as_view(), name='register-open'),
    path('register/approval/', ApprovalRegistrationView.as_view(), name='register-approval'),
    path('approve/<int:pk>/', UserApprovalView.as_view(), name='approve')
]