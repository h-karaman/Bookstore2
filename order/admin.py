from django.contrib import admin

# Register your models here.
from order.models import AlisverisSepeti, Siparis, SiparisUrunu


class AlisverisSepetiAdmin(admin.ModelAdmin):
    list_display = ['book','user','urun_adedi','price','urun_tutari' ]
    list_filter = ['user']

class SiparisUrunuline(admin.TabularInline):
    model = SiparisUrunu
    readonly_fields = ('user', 'book','price','urun_adedi','urun_tutari')
    can_delete = False #silme işlemi yapılamasın diye eklendi.
    extra = 0 #fazaladan kaç satır eklenecek.onun için kullanılır.


class SiparisAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','telefon','sehir','alisveris_tutari','durum']
    list_filter = ['durum']
    readonly_fields = ('user','adres','sehir','ulke','telefon','first_name', 'last_name','ip','alisveris_tutari')
    can_delete = False
    inlines = [SiparisUrunuline]

class SiparisUrunuAdmin(admin.ModelAdmin):
    list_display = ['user', 'book','price','urun_adedi','urun_tutari']
    list_filter = ['user']

admin.site.register(AlisverisSepeti,AlisverisSepetiAdmin)
admin.site.register(Siparis,SiparisAdmin)
admin.site.register(SiparisUrunu,SiparisUrunuAdmin)