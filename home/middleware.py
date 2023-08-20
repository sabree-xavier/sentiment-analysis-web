from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

class AnonymousUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if authentication middleware has added the user attribute
        if hasattr(request, 'user') and not request.user.is_authenticated:
            request.user = AnonymousUser()
