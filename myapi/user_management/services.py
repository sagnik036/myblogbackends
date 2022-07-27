from django.db.models import Q
from myapi.common.repos.services import FetchServices, SaveServices
from .info import *


class UserServices(View):
    @staticmethod
    def fetch_profiles(data):
        # Fetching pagination information
        page_size = data.get("page_size")
        page_number = data.get("page")

        # Making Filter queries
        filter_query = UserServices.add_filter_queries(data)
        # Adding Search Queries
        filter_query = UserServices.add_search_queries(
            data,
            filter_query
        )
        # Making Order Queries
        order_query = UserServices.add_order_queries(data)
        # Fetching related instances
        instances = FetchServices.all_instances(
            "auth",
            "User",
            filter_query=filter_query,
            order_query=order_query,
            page_size=page_size,
            page_number=page_number
        )
        # Making response output
        result = [UserInfo.list_data(instance) for instance in instances]
        return result

    @staticmethod
    def fetchProfileById(instance_id):
        instance = FetchServices.instance_by_id(
            "auth",
            "User",
            instance_id,

        )

        result = UserInfo.details_data(instance)
        return result

    @staticmethod
    def save(data):
        columns = {
            'username' : data.get("username"),
            'password' : data.get("password"),
            'is_staff' : data.get("is_staff"),
            'is_superuser' : data.get("is_superuser")
        }

        instance = SaveServices.save_instance(
            "auth",
            "User",
            columns
        )
        return instance

    @staticmethod
    def add_filter_queries(data):
        filter_query = Q()
        return filter_query

    @staticmethod
    def add_search_queries(data, filter_query):
        search = data.get("search")
        if search:
            filter_query.add(
                Q(name__icontains=search),
                Q.AND
            )
        return filter_query

    @staticmethod
    def add_order_queries(data):
        order_query = ["id"]
        return order_query
