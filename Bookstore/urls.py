"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


import home
import os
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from home import views

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path("book/", include("book.urls")),#book sayfası için url tanıtıldı
    path("home/", include("home.urls")),#anasayfa için url 
    path("iletisim", views.iletisim, name="iletisim"),
    path("", include("home.urls")),#herhangi bir şey yazılmazsa home a gidecektir.
    path('admin/', admin.site.urls), #admin için url tanitildi
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>', views.category_books, name='category_books'),
    path('book/<int:id>/<slug:slug>/', views.book_detail, name='book_detail'),
    path("hakkimizda", views.hakkimizda, name="hakkimizda"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG: # new
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
#ilk önce proje ana dosyasında uploads klasörü oluşturulmalı.Sonra
#( Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) os.import altına eklenmeli.


