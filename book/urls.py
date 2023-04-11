from . import views
from django.urls import path 

urlpatterns = [
    # ex: /book/ 
    path("", views.index, name="index"), 
    
   
]