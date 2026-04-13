import time
from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler

class GlobalRenderer(JSONRenderer):
    """Custom renderer to provide a unified response format for all APIs."""
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        
        response_dict = {
            "success": True if status_code < 400 else False,
            "code": status_code,
            "message": "Success" if status_code < 400 else "Error",
            "timestamp": int(time.time()),
            "data": data
        }
        
        # Handle cases where data might be a simple detail string or empty
        if status_code >= 400 and isinstance(data, dict):
            response_dict["message"] = data.get('detail', 'Validation Error')

        return super().render(response_dict, accepted_media_type, renderer_context)

def custom_exception_handler(exc, context):
    """Global exception handler to intercept errors and wrap them in GlobalRenderer."""
    response = exception_handler(exc, context)
    return response 