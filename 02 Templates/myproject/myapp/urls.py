from django.urls import path

from .views import wish, wish1, greet

urlpatterns = [
    path('wish/', wish, name='wish'),
    path('wish1/', wish1, name='wish1'),
    path('greet/', greet, name='greet'),
]