from django.views import View
from .models import *


class BlogInfo(View):
    @staticmethod
    def list_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["user_id"] = instance.user_id_id
            result["title"] = instance.title
            result["image"] =f"http://localhost:8000/media/{instance.image}"
            result["catagory"] = instance.catagory
            result["summary"] = instance.summary
            result["content"] = instance.content
            result["is_draft"] = instance.is_draft
        return result

    @staticmethod
    def details_data(instance):
        result = {}
        # print(instance)
        if instance:
            result["id"] = instance.id
            result["user_id"] = instance.user_id_id
            result["title"] = instance.title
            result["image"] =f"http://localhost:8000/media/{instance.image}"
            result["catagory"] = instance.catagory
            result["summary"] = instance.summary
            result["content"] = instance.content
            result["is_draft"] = instance.is_draft
        return result



    
   
    
   
