from django.utils.deprecation import MiddlewareMixin
from django.contrib import messages
from django.utils import timezone
from django.contrib.sessions.models import Session

class SessionExpiryNotificationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        session_key = request.session.session_key
        if session_key:
            try:
                session = Session.objects.get(session_key=session_key)
                if session.expire_date < timezone.now():
                    messages.warning(request, "Your session has expired. Please log in again.")
            except Session.DoesNotExist:
                pass
