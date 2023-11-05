from rest_framework.pagination import PageNumberPagination

class UserListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = ('last',)


class WeightPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = ('last',)

class BloodPressurePagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = ('last',)

class NotesPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = ('last',)