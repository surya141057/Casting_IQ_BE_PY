from django.core.paginator import Paginator

class CustomPaginator:
    def __init__(self, queryset, page_size,use_serializer=False):
        self.queryset = queryset
        self.page_size = page_size
        self.use_serializer = use_serializer

    def paginate(self, page_number):
        paginator = Paginator(self.queryset, self.page_size)
        try:
            page_obj = paginator.page(page_number)
            result =  page_obj.object_list if self.use_serializer else list(page_obj.object_list.values()) 
                
            return {
                'status': 'Pass',
                'message': {
                    'current_page': page_obj.number,
                    'total_pages': paginator.num_pages,
                    'results': result
                }
            }
        except Exception as e:
            return {
                'status': 'Fail',
                'message': {
                    'error': str(e)
                }
            }
