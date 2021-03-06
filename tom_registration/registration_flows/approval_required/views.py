import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from tom_common.mixins import SuperuserRequiredMixin
from tom_registration.registration_flows.approval_required.forms import ApproveUserForm
from tom_registration.registration_flows.approval_required.forms import RegistrationApprovalForm

logger = logging.getLogger(__name__)


try:
    REGISTRATION_AUTHENTICATION_BACKEND = settings.REGISTRATION_AUTHENTICATION_BACKEND
except AttributeError:
    REGISTRATION_AUTHENTICATION_BACKEND = ''


# TODO make this view inaccessible when logged in
class ApprovalRegistrationView(CreateView):
    """

    """
    template_name = 'tom_registration/register_user.html'
    success_url = reverse_lazy(settings.TOM_REGISTRATION.get('REGISTRATION_REDIRECT_PATTERN', ''))
    form_class = RegistrationApprovalForm

    def form_valid(self, form):
        super().form_valid(form)
        group, _ = Group.objects.get_or_create(name='Public')
        group.user_set.add(self.object)
        group.save()

        messages.info(self.request, 'Your request to register has been submitted to the administrators.')

        return redirect(self.get_success_url())


class UserApprovalView(SuperuserRequiredMixin, UpdateView):
    """

    """
    model = User
    template_name = 'tom_registration/approve_user.html'
    success_url = reverse_lazy('user-list')
    form_class = ApproveUserForm
