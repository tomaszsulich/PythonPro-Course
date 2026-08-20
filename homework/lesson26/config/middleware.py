from collections.abc import Callable

from django.http import HttpRequest, HttpResponse


class HttpMethodLoggingMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        print(
            f"Otrzymano zapytanie metodą {request.method}."
        )

        response = self.get_response(request)

        return response