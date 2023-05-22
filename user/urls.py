
from django.urls import path
from . import views

urlpatterns = [
    # ex: /home/ 
    path("", views.index, name="user_index"), 
    path('guncelle/', views.kullanici_guncelle, name='kullanici_guncelle'),
    path('parola/', views.kullanici_parola_guncelle, name='kullanici_parola_guncelle'),
]