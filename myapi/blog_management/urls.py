from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
   path('blog/',
    views.BlogView.as_view(),
    name="blogview"
   ),

   path('blog/<int:pk>/',
    views.BlogDetailView.as_view(),
    name="blog_detail_view"
   )
    
]

