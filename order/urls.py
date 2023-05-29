from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alisverissepeti/', views.alisverissepeti, name='alisverissepeti'),
    path('sepeteekle/<int:id>', views.sepeteekle, name='sepeteekle'),
    path('sepettencikar/<int:id>', views.sepettencikar, name='sepettencikar'),
    path('siparisurunu/', views.siparisurunu, name='siparisurunu'),
    path('sepeti_guncelle_artir/<int:id>', views.sepeti_guncelle_artir, name='sepeti_guncelle_artir'),
    path('sepeti_guncelle_azalt/<int:id>', views.sepeti_guncelle_azalt, name='sepeti_guncelle_azalt'),
    path('sepetiguncelle/<int:id>', views.sepetiguncelle, name='sepetiguncelle'),
    path('favorilereekle/<int:id>', views.favorilereekle, name='favorilereekle'),
    path('favorisepeti/', views.favorilerim, name='favorilerim'),
    path('favorisepetindencikar/<int:id>', views.favorisepetindencikar, name='favorisepetindencikar'),
    
             ]