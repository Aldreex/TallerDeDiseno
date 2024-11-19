from django.utils.deprecation import MiddlewareMixin

class SessionMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        print("context_data: ",response.context_data)
        if hasattr(request, "session"):
            response.context_data = response.context_data or {}
            response.context_data["session"] = request.session
        return response