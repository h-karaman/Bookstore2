from django.contrib import admin

from home.models import IletisimMesaji, SayfaAyarlari

# Register your models here.
class IletisimMesajiAdmin(admin.ModelAdmin):
    list_display = ['ad_soyad', 'mesaj','konu', 'durum','guncellenme_tarihi' ]
    readonly_fields =('ad_soyad','konu','email','mesaj','ip')
    list_filter = ['durum']


admin.site.register(SayfaAyarlari)
admin.site.register(IletisimMesaji,IletisimMesajiAdmin)