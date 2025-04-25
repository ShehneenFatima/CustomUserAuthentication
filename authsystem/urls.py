from django.contrib import admin
from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import protected_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='home'),  # Root URL shows login page
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.signup_view, name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('protected/', protected_view),
]
