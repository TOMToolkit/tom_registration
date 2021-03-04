from django import forms

from tom_common.forms import CustomUserCreationForm


# TODO: how will groups be handled in this registration flow? request group membership?
class OpenRegistrationForm(CustomUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('groups')
