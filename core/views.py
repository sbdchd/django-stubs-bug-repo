from django.http import HttpResponse, HttpRequest
from core.models import AnonymousUser

def logout(request: HttpRequest) -> HttpResponse:
    request.session.flush()
    request.user = AnonymousUser()
    return HttpResponse(status=201)
