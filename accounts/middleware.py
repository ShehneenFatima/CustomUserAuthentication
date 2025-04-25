import logging
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

User = get_user_model()

class CustomAuthMiddleware(MiddlewareMixin): #works with both old and new styles of Django middleware.
    def process_request(self, request): #http request object,can be modified before further processing
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            try:
                user = User.objects.get(auth_token=token)
                request.user = user
            except User.DoesNotExist:
                request.user = AnonymousUser()
        else:
            request.user = AnonymousUser()

import logging
from django.utils.deprecation import MiddlewareMixin  # Only if you're using Django <= 1.9
# For Django >= 1.10 use: from django.utils.middleware import MiddlewareMixin

# Create a logger
logger = logging.getLogger('django')  # Use 'django' to integrate with Django's logging system
handler = logging.FileHandler('request_logs.txt')  # File handler to log to 'request_logs.txt'
formatter = logging.Formatter('%(asctime)s - %(message)s')  # Customize the log format
handler.setFormatter(formatter)
logger.addHandler(handler)  # Attach the handler to the logger
logger.setLevel(logging.INFO)  # Set log level to INFO (will log INFO and above)

# Middleware for logging requests
class RequestLoggingMiddleware(MiddlewareMixin):  # Inheriting from MiddlewareMixin for Django < 1.10
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')  # IP address of the user
        method = request.method  # HTTP method (GET, POST, etc.)
        path = request.get_full_path()  # Full path of the URL
        user = request.user if request.user.is_authenticated else 'Anonymous'  # Get user if authenticated
        # Log the request information
        logger.info(f'IP: {ip} | Method: {method} | Path: {path} | User: {user}')
