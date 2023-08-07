from django.urls import path
from . import views

urlpatterns = [
    path('image_upload_view/', views.image_upload_view),
    
    
    # add more URL patterns here
]
