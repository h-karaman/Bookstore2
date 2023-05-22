from django.contrib import admin

from user.models import KullaniciProfili



class KullaniciProfiliAdmin(admin.ModelAdmin):
    list_display = ['kullanici_adi','ulke', 'sehir','telefon','adres','image_tag' ]
    
    
# Register your models here.
admin.site.register(KullaniciProfili,KullaniciProfiliAdmin)
