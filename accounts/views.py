from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm  
from django.http import JsonResponse
#django Rest framework imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile_view(request):
    print(f"User authenticated: {request.user.is_authenticated}")
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Optionally, add custom claims or fields to the token here
        return token

    def validate(self, attrs):
        # Overriding to use email instead of username
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = CustomUser.objects.get(email=email)
                if user.check_password(password):
                    attrs['user'] = user
                else:
                    raise serializers.ValidationError("Invalid credentials")
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("User with this email does not exist.")
        else:
            raise serializers.ValidationError("Email and password are required.")
        
        return attrs

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    

@api_view(['GET'])  # Decorator that makes the function handle only GET requests
@permission_classes([IsAuthenticated])  # Only authenticated users can access this view
def protected_view(request):
    context = {
        'message': f'Hello {request.user.email}, you accessed a protected view!'
    }
    return Response(context)  # This will return a JSON response

    