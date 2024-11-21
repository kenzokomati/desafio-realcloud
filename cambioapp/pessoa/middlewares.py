from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse

ALLOWED_EMAILS = [
    "joanne.carneiro@realcloud.com.br",
    "pedro.alpis@realcloud.com.br",
    "kenzo.komati@gmail.com"
]

class EmailAccessMiddleware:
    """
    Middleware to restrict access based on user email.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ensure the user is logged in
        if request.user.is_authenticated:
            # Check if the user's email is in the allowed list
            if request.user.email not in ALLOWED_EMAILS:
                # Log the user out
                logout(request)
                
                # Add a message to notify the user
                messages.error(request, "You are not authorized to access this application. You have been logged out.")
                
                # Redirect the user to the login page
                return redirect('accounts/google/login/')  # Ensure 'login' is the correct URL name for the login page
        
        # Proceed with the request if no restrictions are applied
        response = self.get_response(request)
        return response
