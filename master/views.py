from rest_framework import generics
from django.http import JsonResponse
from .models import pattern_type
from utils.paginator import CustomPaginator
from .serializer import matchPlate_typeserializer, pattern_typeSerializer
from http import HTTPStatus
from utils.logger import setup_logger
from .models import matchPlate_type

class pattern_typeView(generics.GenericAPIView):
    logger = setup_logger("my_logger")
    def get(self,request):     
        try:
            #company = request.company.id
            is_active = request.GET.get("is_active",True)
            is_draft = request.GET.get("is_draft",False)
            page_no = request.GET.get("page_no",1)
            queryset =pattern_type.objects.filter(is_active=is_active, is_draft=is_draft).order_by('created_date')
            serializer = pattern_typeSerializer(queryset,many=True)
            paginator = CustomPaginator(serializer.data,page_size=5,use_serializer=True)
            response = paginator.paginate(page_no)
            return JsonResponse(response, safe=False)
        except Exception as e:
            self.logger.error(f"Error in GET method: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'fail', 'message': 'Something went wrong. Please try again later'.capitalize().replace('_', ' ')},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR.value)

    def post(self,request):
        try:
            data = request.data
            serializer = pattern_typeSerializer(data=data)
            try:
                is_valid = serializer.is_valid(raise_exception=True)
            except:
                serializer.is_valid()
                errors = serializer.errors
                return JsonResponse({'status': 'fail', 'message': f"Seralizer error {errors}".capitalize().replace('_', ' ')}, status=HTTPStatus.BAD_REQUEST.value)
            if is_valid:
                pattern_type_data = serializer.validated_data
                is_draft = pattern_type_data.get('is_draft', False)
                if  not len(pattern_type_data['name']):
                    return JsonResponse({'status': 'fail', 'message': 'Please Enter Pattern Type Name'.capitalize().replace('_', ' ')},
                                    status=HTTPStatus.BAD_REQUEST.value)

                if pattern_type.objects.filter(is_draft = False, name = pattern_type_data['name']).exists():
                    return JsonResponse({'status': 'fail', 'message': 'Pattern Type Name Already Exist'.capitalize().replace('_', ' ')}, status=HTTPStatus.BAD_REQUEST.value)
                
                pattern_type.objects.create(**pattern_type_data)
                
                message = ('Pattern type saved as draft successfully' if is_draft 
                      else 'Pattern type created successfully')
            
            return JsonResponse(
                {'status': 'success', 'message': message},
                status=HTTPStatus.CREATED.value
            )

        except Exception as e:
            self.logger.error(f"Error in GET method: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'fail', 'message': 'Something went wrong. Please try again later'.capitalize().replace('_', ' ')},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR.value)

    def put(self,request):
        try:
            data = request.data
            id = request.data['id']
            instance = pattern_type.objects.get(id=id)
            serializer = pattern_typeSerializer(instance,data=data)
            try:
                is_valid = serializer.is_valid(raise_exception=True)
            except:
                serializer.is_valid()
                errors = serializer.errors
                return JsonResponse({'status': 'fail', 'message': "Something Went Wrong".capitalize().replace('_', ' ')}, status=HTTPStatus.BAD_REQUEST.value)
            if is_valid:
                pattern_type_data = serializer.validated_data
                is_draft = pattern_type_data.get('is_draft', False)
                if  not len(pattern_type_data['name']):
                    return JsonResponse({'status': 'fail', 'message': 'Please Enter Pattern Type Name'.capitalize().replace('_', ' ')},
                                    status=HTTPStatus.BAD_REQUEST.value)
                if pattern_type.objects.filter(is_draft = False, name = pattern_type_data['name']).exists():
                    return JsonResponse({'status': 'fail', 'message': 'Pattern Type Name Already Exist'.capitalize().replace('_', ' ')}, status=HTTPStatus.BAD_REQUEST.value)
                
                serializer.save()
                message = ('Pattern type update draft successfully' if is_draft 
                      else 'Pattern type update successfully')
            
            return JsonResponse(
                {'status': 'success', 'message': message},
                status=HTTPStatus.CREATED.value
            )

        except Exception as e:
            self.logger.error(f"Error in GET method: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'fail', 'message': 'Something went wrong. Please try again later'.capitalize().replace('_', ' ')},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR.value)

class matchPlate_typeView(generics.GenericAPIView):
    logger = setup_logger("my_logger")
    def get(self,request):     
        try:
            #company = request.company.id
            is_active = request.GET.get("is_active",True)
            is_draft = request.GET.get("is_draft",False)
            page_no = request.GET.get("page_no",1)
            queryset =matchPlate_type.objects.filter(is_active=is_active, is_draft=is_draft).order_by('created_date')
            serializer = matchPlate_typeserializer(queryset,many=True)
            paginator = CustomPaginator(serializer.data,page_size=5,use_serializer=True)
            response = paginator.paginate(page_no)
            return JsonResponse(response, safe=False)
        except Exception as e:
            self.logger.error(f"Error in GET method: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'fail', 'message': 'Something went wrong. Please try again later'.capitalize().replace('_', ' ')},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR.value)
        
    def post(self,request):
        try:
            data = request.data
            serializer = matchPlate_typeserializer(data=data)
            try:
                is_valid = serializer.is_valid(raise_exception=True)
            except:
                serializer.is_valid()
                errors = serializer.errors
                return JsonResponse({'status': 'fail', 'message': f"Seralizer error {errors}".capitalize().replace('_', ' ')}, status=HTTPStatus.BAD_REQUEST.value)
            if is_valid:
                matchPlate_type_data = serializer.validated_data
                is_draft = matchPlate_type_data.get('is_draft', False)
                if  not len(matchPlate_type_data['name']):
                    return JsonResponse({'status': 'fail', 'message': 'Please Enter matchPlate Type Name'.capitalize().replace('_', ' ')},
                                    status=HTTPStatus.BAD_REQUEST.value)

                if matchPlate_type.objects.filter(is_draft = False, name = matchPlate_type_data['name']).exists():
                    return JsonResponse({'status': 'fail', 'message': 'matchPlate Type Name Already Exist'.capitalize().replace('_', ' ')}, status=HTTPStatus.BAD_REQUEST.value)
                
                matchPlate_type.objects.create(**matchPlate_type_data)
                
                message = ('matchPlate type saved as draft successfully' if is_draft 
                      else 'matchPlate type created successfully')
            
            return JsonResponse(
                {'status': 'success', 'message': message},
                status=HTTPStatus.CREATED.value
            )

        except Exception as e:
            self.logger.error(f"Error in GET method: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'fail', 'message': 'Something went wrong. Please try again later'.capitalize().replace('_', ' ')},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR.value)

    def put(self,request):
        try:
            data = request.data
            id = request.data['id']
            instance = matchPlate_type.objects.get(id=id)
            serializer = matchPlate_typeserializer(instance,data=data)
            try:
                is_valid = serializer.is_valid(raise_exception=True)
            except:
                serializer.is_valid()
                errors = serializer.errors
                return JsonResponse({'status': 'fail', 'message': "Something Went Wrong".capitalize().replace('_', ' ')}, status=HTTPStatus.BAD_REQUEST.value)
            if is_valid:
                matchPlate_type_data = serializer.validated_data
                is_draft = matchPlate_type_data.get('is_draft', False)
                if  not len(matchPlate_type_data['name']):
                    return JsonResponse({'status': 'fail', 'message': 'Please Enter matchPlate Type Name'.capitalize().replace('_', ' ')},
                                    status=HTTPStatus.BAD_REQUEST.value)
                if matchPlate_type.objects.filter(is_draft = False, name = matchPlate_type_data['name']).exists():
                    return JsonResponse({'status': 'fail', 'message': 'matchPlate Type Name Already Exist'.capitalize().replace('_', ' ')}, status=HTTPStatus.BAD_REQUEST.value)
                
                serializer.save()
                message = ('matchPlate type update draft successfully' if is_draft 
                      else 'matchPlate type update successfully')
            
            return JsonResponse(
                {'status': 'success', 'message': message},
                status=HTTPStatus.CREATED.value
            )

        except Exception as e:
            self.logger.error(f"Error in GET method: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'fail', 'message': 'Something went wrong. Please try again later'.capitalize().replace('_', ' ')},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR.value)
