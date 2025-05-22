# myapp/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Item
from django.forms import model_to_dict

def get_items(request):
    items = Item.objects.all()
    data = {"items": list(items.values())}
    return JsonResponse(data)

def get_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    data = {"item": model_to_dict(item)}
    return JsonResponse(data)
