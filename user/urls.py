
from django.urls import path
from . import views

urlpatterns = [
    # ex: /home/ 
    path("", views.index, name="user_index"), 
    path('guncelle/', views.kullanici_guncelle, name='kullanici_guncelle'),
    path('parola/', views.kullanici_parola_guncelle, name='kullanici_parola_guncelle'),
    path('siparisler/', views.kullanici_siparisleri, name='kullanici_siparisleri'),
    path('alisverisdetayi/<int:id>/', views.kullanici_siparis_urunleri_detayi, name='kullanici_siparis_urunleri_detayi'),
    path('yorumlar/', views.kullanici_yorumlari, name='kullanici_yorumlari'),
    path('yorumsil/<int:id>/', views.yorum_sil, name='yorum_sil'),
    
    
]