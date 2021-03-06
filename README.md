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

    To prevent logged-in users from accessing the registration page, add `RedirectAuthenticatedUsersFromRegisterMiddleware` to the `MIDDLEWARE` settings:

    ```python
    MIDDLEWARE = [
        ...
        'tom_common.middleware.AuthStrategyMiddleware',
        'tom_registration.middleware.RedirectAuthenticatedUsersFromRegisterMiddleware',
    ]
    ```

3. Depending on your preferred registration flow, include the appropriate tom_registration URLconf in your project `urls.py`. You will need to ensure that this urlpattern appears in the list before your `tom_common.urls`.

Open Registration:

    ```python
        urlpatterns = [
            ...
            path('', include('tom_registration.registration_flows.open.urls', namespace='registration')),
        ]
    ```

Approval Registration:

    ```python
        urlpatterns = [
            ...
            path('', include('tom_registration.registration_flows.approval_required.urls', namespace='registration')),
        ]
    ```

# TODO: Add links to the correct files
4. While the registration views are now accessible directly, some changes need to be made to templates to make them available.

Copy the contents of the following file to `templates/tom_common/partials/navbar_login.html`.

If you're using approval registration, copy the contents of this file to `templates/auth/user_list.html`.

5. If you're using approval registration and you would like a message informing the user that their account is pending approval if they try to log in prior to approval, you'll need to make the following changes:

First, in your `settings.py`, set the first item of your `AUTHENTICATION_BACKENDS`:

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

## Running the tests

In order to run the tests, run the following in your virtualenv:

`python manage.py test`
