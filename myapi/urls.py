from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    
    path('',include('myapi.user_management.urls')),
    path('',include('myapi.blog_management.urls'))
]
