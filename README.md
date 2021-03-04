# TOM Registration

This reusable TOM Toolkit app provides support for two user registration flows in the TOM Toolkit.

The two registration flows are as follows:

1. Open Registration - In this flow, the user fills in a registration form and is immediately able to access the TOM as a member of the Public Group.

2. Approval Registration - In this flow, the user fills in a registration form, and is inactive until an administrator reviews and approves their registration.

## Installation

1. Install the package into your TOM environment:
    ```bash
    pip install tom_registration
   ```

2. In your project `settings.py`, add `tom_registration` to your `INSTALLED_APPS` setting:

    ```python
    INSTALLED_APPS = [
        ...
        'tom_registration',
    ]
    ```

    And add the follow setting, with appropriate values for your use case:

    ```python
    TOM_REGISTRATION = {
        'REGISTRATION_AUTHENTICATION_BACKEND': 'django.contrib.auth.backends.ModelBackend',
        'REGISTRATION_REDIRECT_PATTERN': 'home'
    }
    ```

    If you're using approval registration and you would like a message informing the user that their account is pending approval if they try to log in prior to approval, you'll need to make the following changes to your `settings.py`. First, set the first item of your `AUTHENTICATION_BACKENDS`:

    ```python
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.AllowAllUsersModelBackend',
        'guardian.backends.ObjectPermissionBackend'
    )
    ```

    Then, change the value of `REGISTRATION_AUTHENTICATION_BACKEND` in the `TOM_REGISTRATION` setting that was just created:

    ```python
    TOM_REGISTRATION = {
        'REGISTRATION_AUTHENTICATION_BACKEND': 'django.contrib.auth.backends.AllowAllUsersModelBackend`,
        ...
    }
    ```

3. Depending on your preferred registration flow, include the appropriate tom_registration URLconf in your project `urls.py`.

Open Registration:

    ```python
        urlpatterns = [
            ...
            path('', include('tom_registration.registration_flows.open.urls'), name='registration'),
        ]
    ```

Approval Registration:

    ```python
        urlpatterns = [
            ...
            path('', include('tom_registration.registration_flows.approval_required.urls'), name='registration'),
        ]
    ```

4. While the registration views are now accessible directly, some changes need to be made to templates to make them available.

Copy the contents of the following file to `templates/tom_registration/navbar_login.html`.

If you're using approval registration, copy the contents of this file to `templates/tom_common/auth/partials/user_list.html`.


## Running the tests

In order to run the tests, run the following in your virtualenv:

`python manage.py test`

