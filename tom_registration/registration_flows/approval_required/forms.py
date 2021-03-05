from django import forms
from django.contrib.auth.forms import AuthenticationForm

from tom_common.forms import CustomUserCreationForm


class RegistrationApprovalForm(CustomUserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if self.cleaned_data['password1']:  # TODO: what is this?
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            self.save_m2m()

        return user


class ApproveUserForm(CustomUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password1')
        self.fields.pop('password2')

    def save(self, commit=True):
        user = super(forms.ModelForm, self).save(commit=False)  # TODO: document explicit call to forms.ModelForm superclass
        user.is_active = True
        if commit:
            user.save()
            self.save_m2m()

        return user


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        print('confirm_login_allowed')
        if not user.is_active:
            raise forms.ValidationError(
                ('Your registration is currently pending administrator approval.'),
                code='inactive'
            )
