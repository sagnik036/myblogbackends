from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","is_superuser","is_staff"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)