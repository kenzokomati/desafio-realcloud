from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.utils.text import slugify

ALLOWED_EMAILS = [
    "joanne.carneiro@realcloud.com.br",
    "pedro.alpis@realcloud.com.br",
    "kenzo.komati@gmail.com",
    "ekkomati0@gmail.com",
]

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Automatically associate the social login with an existing user if the email matches,
        and restrict access based on a whitelist.
        """
        user = sociallogin.user
        email = user.email

        # Check if the email is authorized
        if email not in ALLOWED_EMAILS:
            messages.error(request, "Your email is not authorized to access this application.")
            return redirect(reverse('unauthorized'))  # Redirect to custom error page

        # Check if a user already exists with this email
        try:
            existing_user = User.objects.get(email=email)
            # Link the social login to the existing user
            sociallogin.connect(request, existing_user)
        except User.DoesNotExist:
            # If no user exists with this email, create a new user
            base_username = slugify(user.email.split('@')[0])  # Use part of the email as the base username
            username = base_username

            user.username = username
            user.set_unusable_password()  # Ensure no password is set for social accounts
            user.save()
    
    def get_login_redirect_url(self, request):
        """
        Redirect to home page after successful login.
        """
        return reverse('home')
