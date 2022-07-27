from django.views import View
from .models import *


class UserInfo(View):
    @staticmethod
    def list_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["username"] = instance.username
            result["password"]=instance.password
        return result

    @staticmethod
    def details_data(instance):
        result = {}
        # print(instance)
        if instance:
            result["id"] = instance.id
            result["username"] = instance.username
            result["password"]=instance.password
        return result



    
   
    
   
