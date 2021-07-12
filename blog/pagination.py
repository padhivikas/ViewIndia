from rest_framework.pagination import PageNumberPagination

class BlogPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "records"