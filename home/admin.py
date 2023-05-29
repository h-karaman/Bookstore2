from django.contrib import admin

from home.models import IletisimMesaji,SayfaAyarlari,FAQ

# Register your models here.
class IletisimMesajiAdmin(admin.ModelAdmin):
    list_display = ['ad_soyad', 'mesaj','konu','email','durum','guncellenme_tarihi' ]
    readonly_fields =('ad_soyad','konu','email','mesaj','ip')
    list_filter = ['durum']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['soru', 'cevap','ordernumber','durum']
    list_filter = ['durum']   
    
    


admin.site.register(SayfaAyarlari)
admin.site.register(IletisimMesaji,IletisimMesajiAdmin)
admin.site.register(FAQ,FAQAdmin)

