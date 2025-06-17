from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product, Category, Order

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products':products, 'categories':categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "store/category_products.html", {"category": category})

def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'store/order_summary.html', {'order':order})