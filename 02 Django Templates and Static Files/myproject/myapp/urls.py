from django.urls import path

from .views import wish


urlpatterns = [
    path("wish/", wish, name='wish')
]