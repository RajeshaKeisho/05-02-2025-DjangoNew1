from django.urls import path
from .views import registration, login, logout

urlpatterns = [
    # path('display/', display, name='display'),
    path("registration/", registration, name="morning"),
    path("login/", login, name="morning"),
    path("logout/", logout, name="morning"),
]