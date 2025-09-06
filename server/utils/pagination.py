from rest_framework.pagination import PageNumberPagination


class PageNumberWithSizePagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 1000

    def paginate_queryset(self, queryset, request, view=None):
        # view is not None
        # getattr(view, 'page_size', None)
        # page_size is int
        if (
            view is not None
            and (page_size := getattr(view, "page_size", None))
            and isinstance(page_size, int)
        ):
            self.page_size = page_size

        return super().paginate_queryset(queryset, request, view)
