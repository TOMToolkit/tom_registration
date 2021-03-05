from django.shortcuts import redirect
from django.urls import reverse


class RedirectAuthenticatedUsersFromRegisterMiddleware:
    """
    Middleware used to redirect authenticated users away from the register page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path_info == '/accounts/register/':
            return redirect(reverse('user-update', kwargs={'pk': request.user.id}))

        return self.get_response(request)
