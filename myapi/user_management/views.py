# Common Imports
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
# Module Imports
from myapi.common.serializers.serializers import MasterListFilterBackend
from myapi.common.responses.error_response import FormatResponses
from .services import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken

class UserView(GenericAPIView):
    serializer_class = UserSerializers
    filter_backends = (MasterListFilterBackend,)
    permission_classes = []
  
    @classmethod
    def get(cls, request):
        data = request.GET
        token_str = data.get('token')
        access_token = AccessToken(token_str)
        user = User.objects.get(id=access_token['user_id'])
        response = {
                "username": user.username,
                
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def post(cls, request,):
        validate_data = UserSerializers(data=request.data)
        is_valid = validate_data.is_valid()
        if is_valid:
            data = validate_data.validated_data
            
            instance = validate_data.save()
            user = User.objects.get(username=validate_data.data['username'])
            refresh = RefreshToken.for_user(user)
            response = {
                "result": instance.id,
                "message": "User Created successfully.",
                "token"  : str(refresh.access_token)
            }
            status_code = status.HTTP_200_OK
        else:
            errors = FormatResponses.error_response(validate_data.errors)
            response = {"errors": errors}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)