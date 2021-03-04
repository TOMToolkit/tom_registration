from django.urls import path

from .views import ApprovalRegistrationView, UserApprovalView

app_name = 'tom_registration'


urlpatterns = [
    path('register/', ApprovalRegistrationView.as_view(), name='register'),
    path('approve/<int:pk>/', UserApprovalView.as_view(), name='approve')
]