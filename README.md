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


## Running the tests

In order to run the tests, run the following in your virtualenv:

`python tom_superevent/tests/run_tests.py`

