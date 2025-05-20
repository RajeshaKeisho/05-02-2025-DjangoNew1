from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

class CustomerPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'

class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 8
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 50

class OrderCursorPagination(CursorPagination):
    page_size = 6
    ordering = '-order_date'
    cursor_query_param = 'cursor'


# Frontend Pagination:
from django.core.paginator import Paginator

class CustomPaginator:
    def __init__(self, queryset, per_page=10, limit=None, offset=0, cursor=None):
        self.queryset = queryset
        self.per_page = per_page
        self.limit = limit
        self.offset = offset
        self.cursor = cursor
    
    def get_page(self):
        if self.limit is not None:
            # LimitOffset style
            end = self.offset + self.limit
            return list(self.queryset[self.offset:end])
        elif self.cursor is not None:
            # Cursor style (simplified)
            try:
                cursor_pos = int(self.cursor)
            except (ValueError, TypeError):
                cursor_pos = 0
            
            start = cursor_pos
            end = cursor_pos + self.per_page
            return list(self.queryset[start:end])
        else:
            # PageNumber style
            paginator = Paginator(self.queryset, self.per_page)
            return paginator.page(1)
    
    def get_next_cursor(self):
        if self.cursor is not None:
            try:
                return str(int(self.cursor) + self.per_page)
            except (ValueError, TypeError):
                return str(self.per_page)
        return None
    
    def get_prev_cursor(self):
        if self.cursor is not None:
            try:
                prev = max(0, int(self.cursor) - self.per_page)
                return str(prev) if prev > 0 else None
            except (ValueError, TypeError):
                return None
        return None