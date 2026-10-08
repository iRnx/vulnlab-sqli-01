from django.http import HttpResponseForbidden


class LocalOnlyMiddleware:
    ALLOWED_IPS = {
        "127.0.0.1",
        "::1",
    }

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        remote_addr = request.META.get("REMOTE_ADDR", "")

        if remote_addr not in self.ALLOWED_IPS:
            return HttpResponseForbidden(
                "VulnLab é intencionalmente vulnerável e só pode ser usado localmente."
            )

        return self.get_response(request)
