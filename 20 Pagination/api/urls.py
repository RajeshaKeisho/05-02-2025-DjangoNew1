# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     CustomerListView,
#     CustomerDetailView,
#     ProductViewSet,
#     OrderListView,
#     OrderDetailView
# )

# router = DefaultRouter()
# router.register(r'products', ProductViewSet)

# urlpatterns = [
#     path('customers/', CustomerListView.as_view(), name='customer-list'),
#     path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
#     path('orders/', OrderListView.as_view(), name='order-list'),
#     path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
#     path('', include(router.urls)),


    
# ]

# Frontend:
from django.urls import path
from .views import (
    customer_list, customer_detail,
    product_list, product_detail,
    order_list, order_detail
)

urlpatterns = [
    # Customer URLs
    path('customers/', customer_list, name='customer-list'),
    path('customers/<int:pk>/', customer_detail, name='customer-detail'),
    
    # Product URLs
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    
    # Order URLs
    path('orders/', order_list, name='order-list'),
    path('orders/<int:pk>/', order_detail, name='order-detail'),
]