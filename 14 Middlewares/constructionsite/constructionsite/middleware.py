from django.http import HttpResponse
from django.conf import settings
import logging

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if site is under construction
        # Ensures that users can still access the /under_construction/ page.
        if request.path != '/under_construction/' and settings.SITE_UNDER_CONSTRUCTION:
            return HttpResponse("Site under construction. Please check back later.")
        
        response = self.get_response(request)
        return response


    
class FooterAppendMiddleware:
    """
    Middleware to append a footer message to the HTML response content.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request
        response = self.get_response(request)
        
        # Check if the response is an HTML response
        if 'text/html' in response.get('Content-Type', ''):
            # Modify the content by appending a footer message
            footer_message = "<footer><p>Powered by Django</p></footer>"
            content = response.content.decode('utf-8')  # Convert bytes to string
            content = content.replace("</body>", f"{footer_message}</body>")  # Append footer before closing body tag
            response.content = content.encode('utf-8')  # Convert back to bytes
            
        return response


logger = logging.getLogger(__name__)

class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Process the request normally
            response = self.get_response(request)
            return response
        except ValueError as e:
            # Handle ValueError specifically
            logger.error(f"ValueError occurred: {e}")
            return HttpResponse("A ValueError occurred. Please check your input.", status=400)
        except Exception as e:
            # Handle any other exception
            logger.error(f"An unexpected error occurred: {e}")
            return HttpResponse("An unexpected error occurred. Please try again later.", status=500)
