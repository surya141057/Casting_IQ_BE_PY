from rest_framework import generics
from django.http import JsonResponse
from module.models import Module
from utils.paginator import CustomPaginator
from module.serializer import ModuleWithSubmodulesSerializer
from http import HTTPStatus
from utils.logger import setup_logger

class ModuleView(generics.GenericAPIView):
    logger = setup_logger("module")
    def get(self,request):     
        try:
            page_no = request.GET.get("page_no",1)
            modules = Module.objects.prefetch_related('submodule_set')
            serializer = ModuleWithSubmodulesSerializer(modules, many=True)
            paginator = CustomPaginator(serializer.data,page_size=5,use_serializer=True)
            response = paginator.paginate(page_no)
            return JsonResponse(response, safe=False)
        except Exception as e:
            self.logger.error(f"Error in GET method: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'fail', 'message': 'Something went wrong. Please try again later'.capitalize().replace('_', ' ')},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR.value)