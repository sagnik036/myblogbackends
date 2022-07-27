# Common Imports
from rest_framework import serializers
from .models import (
    Myblog
)


class MyBlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Myblog
        fields = "__all__"
