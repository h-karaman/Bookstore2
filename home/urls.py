from . import views
from django.urls import path 

urlpatterns = [
    # ex: /home/ 
    path("", views.index, name="index"), 
    
   
]