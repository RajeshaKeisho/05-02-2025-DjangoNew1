import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name')
    brand = django_filters.CharFilter(field_name='brand__name')
    in_stock = django_filters.BooleanFilter(field_name='stock', lookup_expr='gt', 
                                         label="In Stock", method='filter_in_stock')

    class Meta:
        model = Product
        fields = ['category', 'brand', 'stock', 'min_price', 'max_price']

    def filter_in_stock(self, queryset, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset