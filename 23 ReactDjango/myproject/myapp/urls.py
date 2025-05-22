# myapp/urls.py
from django.urls import path
from .views import get_items, get_item

urlpatterns = [
    path('api/items/', get_items, name='get_items'),
    path('api/items/<int:item_id>/', get_item, name='get_item'),
]
