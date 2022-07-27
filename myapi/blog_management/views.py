# Common Imports
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
# Module Imports
from myapi.common.serializers.serializers import MasterListFilterBackend
from myapi.common.responses.error_response import FormatResponses
from .services import *
from .serializers import *
from rest_framework.permissions import *


class BlogView(GenericAPIView):
    serializer_class = MyBlogSerializers
    filter_backends = (MasterListFilterBackend,)
    permission_classes=[AllowAny]

    @classmethod
    def get(cls, request):
        data = request.GET
        response = MyBlogServices.fetch_profiles(data)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def post(cls, request,):
        validate_data = MyBlogSerializers(data=request.data)
        is_valid = validate_data.is_valid()
        if is_valid:
            data = validate_data.validated_data
            instance = MyBlogServices.save(data)
            response = {
                "result": instance.id,
                "message": "Blog Added successfully."
            }
            status_code = status.HTTP_200_OK
        else:
            errors = FormatResponses.error_response(validate_data.errors)
            response = {"errors": errors}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)


class BlogDetailView(GenericAPIView):
    serializer_class = MyBlogSerializers
    filter_backends = (MasterListFilterBackend,)
    permission_classes = [AllowAny]

    @classmethod
    def get(cls, request, pk):
        response = MyBlogServices.fetchProfileById(pk)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def put(cls, request, pk):
        validate_date = MyBlogSerializers(data=request.data)
        is_valid = validate_date.is_valid()
        if is_valid:
            data = validate_date.validated_data
            MyBlogServices.update(pk, data)
            response = {
                "message": "Updated Successfully"
            }
            
            status_code = status.HTTP_200_OK
            return Response(response, status=status_code)

        else:
            errors = FormatResponses.error_response(validate_date.errors)
            response = {
                "errors": errors
            }

            status_code = status.HTTP_400_BAD_REQUEST
            return Response(response, status_code)

    @classmethod
    def delete(cls, request, pk):
        MyBlogServices.delete(pk)
        response = {
            "message": "Deleted Successfully"
        }
        
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
