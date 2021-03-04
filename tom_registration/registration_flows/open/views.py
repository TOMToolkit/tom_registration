import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from tom_registration.forms import OpenRegistrationForm

logger = logging.getLogger(__name__)


try:
    REGISTRATION_AUTHENTICATION_BACKEND = settings.REGISTRATION_AUTHENTICATION_BACKEND
except AttributeError:
    REGISTRATION_AUTHENTICATION_BACKEND = ''


# TODO make this view inaccessible when logged in
class OpenRegistrationView(CreateView):
    """

    """
    template_name = 'tom_registration/register_user.html'
    success_url = reverse_lazy(settings.TOM_REGISTRATION.get('REGISTRATION_REDIRECT_PATTERN', ''))
    form_class = OpenRegistrationForm

    def form_valid(self, form):
        print('form valid')
        super().form_valid(form)
        group, _ = Group.objects.get_or_create(name='Public')
        group.user_set.add(self.object)
        group.save()

        messages.info(self.request, 'Registration was successful!')
        if isinstance(self.object, User):
            try:
                print('pre-login')
                # TODO: how do we ensure that the model backend is in use in settings.py?
                login(self.request, self.object, backend=REGISTRATION_AUTHENTICATION_BACKEND)
                print('login')
            except ValueError as ve:
                logger.error(f'Unable to log in newly registered user: {ve}')

        return redirect(self.get_success_url())