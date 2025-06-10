from django.urls import path
from .views import moringn_message, afternoon_message, evening_message, message

urlpatterns = [
    # path('display/', display, name='display'),
    path("morning/", moringn_message, name="morning"),
    path("noon/", afternoon_message, name="morning"),
    path("evening/", evening_message, name="morning"),
    path("message/", message, name="message"),
]