from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse

ALLOWED_EMAILS = [
    "joanne.carneiro@realcloud.com.br",
    "pedro.alpis@realcloud.com.br",
    "kenzo.komati@gmail.com",
]

class EmailAccessMiddleware:
    """
    Middleware to restrict access based on user email.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.email not in ALLOWED_EMAILS:
                logout(request)
                messages.error(request, "You are not authorized to access this application. You have been logged out.")
                return redirect('landingpage')  # Redirect unauthorized users to the landing page
        
        response = self.get_response(request)
        return response
