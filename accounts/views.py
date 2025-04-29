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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): #Creating serializer controling how JWT tokens are issued
    @classmethod
    def get_token(cls, user):#a method to customize token,adding more fields,get_token=customize tokens
        token = super().get_token(user) #invokes the parent class .get_token method,to get base jwt token for user
        # Add custom fields to the token
        token['email'] = user.email  # Add user's email
        return token

    def validate(self, attrs): #check if email and password,provided,validate?
        # Overriding to use email 
        email = attrs.get('email')
        password = attrs.get('password') #extracting...

        if email and password: #check if both are provided?
            try:
                user = CustomUser.objects.get(email=email) #Trying to find a user in the database based on email (not username).
                if user.check_password(password): #matches password
                    attrs['user'] = user #Attaching found user to validated data (attrs)
                else:
                    raise serializers.ValidationError("Invalid credentials")
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("User with this email does not exist.")
        else:
            raise serializers.ValidationError("Email and password are required.")
        
        return attrs #Return the validated attributes,now attached with the user.

class CustomTokenObtainPairView(TokenObtainPairView):#connecting the custom serializer to the view that issues tokens.
    serializer_class = CustomTokenObtainPairSerializer #When user hits this endpoint, it will use email + password for authentication.

@api_view(['GET'])  
@permission_classes([IsAuthenticated])  
def protected_view(request):
    context = {
        'message': f'Hello {request.user.email}, you accessed a protected view!'
    }
    # Returning the response
    return Response(context)

