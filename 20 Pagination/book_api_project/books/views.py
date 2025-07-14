from rest_framework import generics, pagination
from .models import Book
from .serializers import BookSerializer

class BookPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookLimitOffsetPagination(pagination.LimitOffsetPagination):
    # default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100

class BookCursorPagination(pagination.CursorPagination):
    page_size = 10
    ordering = 'title'

class BookListViewPageNumber(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPageNumberPagination

class BookListViewLimitOffset(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookLimitOffsetPagination

class BookListViewCursor(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookCursorPagination



# from django.views.generic import ListView
# from .models import Book
# from .pagination import LimitOffsetPaginator, CursorPaginator

# class BookListViewPageNumber(ListView):
#     model = Book
#     template_name = 'books/book_list_pagenumber.html'
#     context_object_name = 'book_list'
#     paginate_by = 10


# class BookListViewLimitOffset(ListView):
#     model = Book
#     template_name = 'books/book_list_limitoffset.html'
#     context_object_name = 'book_list'
#     paginate_by = 10  # Default pagination limit

#     def paginate_queryset(self, queryset, page_size):
#         limit = int(self.request.GET.get('limit', page_size))
#         offset = int(self.request.GET.get('offset', 0))
#         paginator = LimitOffsetPaginator(queryset, limit=limit, offset=offset)
        
#         # Calculate the current page number
#         current_page_number = (offset // limit) + 1
#         page_obj = paginator.get_page(current_page_number)
#         is_paginated = paginator.count > limit
        
#         return paginator, page_obj, page_obj.object_list, is_paginated

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         paginator, page_obj, object_list, is_paginated = self.paginate_queryset(self.object_list, self.paginate_by)
        
#         # Calculate the last offset
#         limit = int(self.request.GET.get('limit', self.paginate_by))
#         last_offset = max(0, paginator.count - limit)
        
#         # Add pagination details to the context
#         context['paginator'] = paginator
#         context['page_obj'] = page_obj
#         context['object_list'] = object_list
#         context['is_paginated'] = is_paginated
#         context['limit'] = limit  # Add the limit to the context
#         context['offset'] = int(self.request.GET.get('offset', 0))  # Add the offset to the context
#         context['last_offset'] = last_offset
#         return context

# from django.views.generic import TemplateView
# from .pagination import CursorPaginator  # Assuming it's in pagination.py


# class BookListViewCursor(TemplateView):
#     template_name = 'books/book_list_cursor.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cursor = self.request.GET.get('cursor')
#         paginator = CursorPaginator(Book.objects.all(), cursor=cursor, per_page=10)
#         page_data = paginator.get_page()

#         context['book_list'] = page_data['results']
#         context['next'] = page_data['next_cursor']
#         context['previous'] = page_data['previous_cursor']
#         context['results'] = page_data['results']
#         return context
