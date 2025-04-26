from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm  # Import your custom user creation form
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def login_view(request):
    next_url = request.GET.get('next', 'profile')  # Default to 'profile' if no next parameter is passed
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url)  # Redirect the user to their intended page after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form, 'next': next_url})


# View for the signup page
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

# View for the user profile page (requires login)
@login_required
def profile_view(request):
    print(f"User authenticated: {request.user.is_authenticated}")
    return render(request, 'profile.html')


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': f'Hello {request.user.email}, you accessed a protected view!'})


