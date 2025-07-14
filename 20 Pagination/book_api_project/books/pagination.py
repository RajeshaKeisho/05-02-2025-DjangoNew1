from django.core.paginator import Paginator, Page

class LimitOffsetPage(Page):
    def has_next(self):
        return self.number < self.paginator.num_pages

    def has_previous(self):
        return self.number > 1

    def next_page_number(self):
        return self.paginator.num_pages

    def previous_page_number(self):
        return 1

class LimitOffsetPaginator(Paginator):
    def __init__(self, object_list, limit=None, offset=0):
        self.limit = int(limit) if limit is not None else len(object_list)
        self.offset = int(offset)
        super().__init__(object_list, self.limit)

    def _get_page(self, *args, **kwargs):
        return LimitOffsetPage(*args, **kwargs)

    def page(self, number):
        bottom = self.offset
        top = bottom + self.per_page
        return self._get_page(self.object_list[bottom:top], number, self)
    
    

from django.core.paginator import Page
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str


class CursorPaginator:
    def __init__(self, queryset, cursor=None, per_page=10):
        self.queryset = queryset.order_by('id')  # Ensure consistent order
        self.cursor = self.decode_cursor(cursor)
        self.per_page = per_page

    def decode_cursor(self, cursor):
        try:
            if cursor:
                return int(force_str(urlsafe_base64_decode(cursor)))
        except Exception:
            return None
        return None

    def encode_cursor(self, value):
        return urlsafe_base64_encode(force_bytes(str(value)))

    def get_page(self):
        if self.cursor:
            items = self.queryset.filter(id__gt=self.cursor)[:self.per_page + 1]
        else:
            items = self.queryset.all()[:self.per_page + 1]

        has_next = len(items) > self.per_page
        results = list(items[:self.per_page])
        next_cursor = self.encode_cursor(results[-1].id) if has_next else None
        previous_cursor = self.encode_cursor(results[0].id) if self.cursor else None

        return {
            'results': results,
            'next_cursor': next_cursor,
            'previous_cursor': previous_cursor,
        }
