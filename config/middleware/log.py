from django.utils.translation import gettext as _

class TranslateLogMessagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def translate(self, message):
        if isinstance(message, str):
            return _(message)
        return message
