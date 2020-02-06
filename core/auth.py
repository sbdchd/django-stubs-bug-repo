from typing import Callable, Any
from functools import wraps

from django.http import HttpRequest, HttpResponse
from django.core.exceptions import PermissionDenied


def login_required(view_func: Callable) -> Callable:
    @wraps(view_func)
    def wrapped_view(
        request, *args, **kwargs
    ) -> Any:
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("authentication required")

    return wrapped_view
