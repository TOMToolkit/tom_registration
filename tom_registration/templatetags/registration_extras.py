from django import template
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse

register = template.Library()


@register.inclusion_tag('tom_registration/partials/register_button.html')
def registration_button():
    """

    """
    return

@register.inclusion_tag('tom_registration/partials/pending_users.html', takes_context=True)
def pending_users(context):
    """

    """
    return {
        'request': context['request'],  # TODO: should this live in the user_list.html template?
        'users': User.objects.filter(is_active=False)
    }
