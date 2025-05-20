from rest_framework import generics, viewsets
from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from .pagination import (
    CustomerPagination,
    ProductLimitOffsetPagination,
    OrderCursorPagination
)

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = ProductLimitOffsetPagination

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderCursorPagination

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



# Frontend View 
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer, Product, Order
from .pagination import CustomPaginator

# Customer Views
def customer_list(request):
    customers = Customer.objects.all().order_by('id')
    
    # PageNumber Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(customers, 5)  # 5 items per page
    
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)
    
    return render(request, 'api/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'api/customer_detail.html', {'customer': customer})

# Product Views
def product_list(request):
    products = Product.objects.all().order_by('id')
    
    # Get limit from request or use default
    try:
        limit = int(request.GET.get('limit', 8))
    except ValueError:
        limit = 8
    
    # Get offset from request or use default
    try:
        offset = int(request.GET.get('offset', 0))
    except ValueError:
        offset = 0
    
    paginator = CustomPaginator(products, limit=limit, offset=offset)
    page_products = paginator.get_page()
    
    return render(request, 'api/product_list.html', {
        'products': page_products,
        'next_offset': offset + limit if offset + limit < len(products) else None,
        'prev_offset': max(0, offset - limit),
        'limit': limit,  # Make sure to pass limit to template
        'offset': offset  # Pass offset as well for clarity
    })

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'api/product_detail.html', {'product': product})

# Order Views
def order_list(request):
    orders = Order.objects.all().order_by('-order_date')
    
    # Cursor Pagination simulation
    cursor = request.GET.get('cursor', None)
    per_page = 6
    
    paginator = CustomPaginator(orders, per_page=per_page, cursor=cursor)
    page = paginator.get_page()
    
    return render(request, 'api/order_list.html', {
        'orders': page,
        'next_cursor': paginator.get_next_cursor(),
        'prev_cursor': paginator.get_prev_cursor()
    })

def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    return render(request, 'api/order_detail.html', {'order': order})