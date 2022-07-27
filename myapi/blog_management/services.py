from django.db.models import Q
from myapi.common.repos.services import FetchServices, SaveServices
from .info import *


class MyBlogServices(View):
    @staticmethod
    def fetch_profiles(data):
        # Fetching pagination information
        page_size = data.get("page_size")
        page_number = data.get("page")

        # Making Filter queries
        filter_query = MyBlogServices.add_filter_queries(data)
        # Adding Search Queries
        filter_query = MyBlogServices.add_search_queries(
            data,
            filter_query
        )
        # Making Order Queries
        order_query = MyBlogServices.add_order_queries(data)
        # Fetching related instances
        instances = FetchServices.all_instances(
            "myapi",
            "Myblog",
            filter_query=filter_query,
            order_query=order_query,
            page_size=page_size,
            page_number=page_number
        )
        # Making response output
        result = [BlogInfo.list_data(
            instance) for instance in instances]
        return result

    @staticmethod
    def fetchProfileById(instance_id):
        instance = FetchServices.instance_by_id(
            "myapi",
            "Myblog",
            instance_id,
        )

        result = BlogInfo.details_data(instance)
        return result

    @staticmethod
    def save(data):
        columns = {
            'title': data.get("title"),
            'user_id': data.get("user_id"),
            'catagory': data.get("catagory"),
            'summary': data.get("summary"),
            'content': data.get("content")
        }

        instance = SaveServices.save_instance(
            "myapi",
            "Myblog",
            columns
        )
        return instance

    @staticmethod
    def update(instance_id, data):
        columns = {
            'title': data.get("title"),
            'user_id_id': data.get("user_id"),
            'catagory': data.get("catagory"),
            'summary': data.get("summary"),
            'content': data.get("content")
        }

        filter_query = Q(
            id=instance_id
        )

        instance = SaveServices.update_instance(
            "myapi",
            "Myblog",
            filter_query,
            columns,
        )

        return instance

    @staticmethod
    def delete(instance_id):
        filter_query = Q(
            id=instance_id
        )

        SaveServices.delete_instances(
            "myapi",
            "Myblog",
            filter_query
        )

        return True

    @staticmethod
    def add_filter_queries(data):
        filter_query = Q()
        return filter_query

    @staticmethod
    def add_search_queries(data, filter_query):
        search = data.get("search")
        if search:
            filter_query.add(
                Q(user_id_id=search),
                Q.AND
            )
        return filter_query

    @staticmethod
    def add_order_queries(data):
        order_query = ["id"]
        return order_query
