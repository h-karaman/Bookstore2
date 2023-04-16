from django.contrib import admin


from book.models import BookCategory, Books, Resimler, Yorumlar


class BooksResimlerInline(admin.TabularInline):
    model = Resimler
    extra = 3   
    readonly_fields = ('image_tag',)
    
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name','bookcategory', 'status','availability','image_tag']
    list_filter = ['bookcategory']
    readonly_fields = ('image_tag',)
    inlines= [BooksResimlerInline]
    prepopulated_fields = {'slug': ('title',)}
    
    
    

class YorumlarAdmin(admin.ModelAdmin):
    list_display = ['konu','yorum', 'durum','olusturulma_zamani']
    list_filter = ['durum']
    readonly_fields = ('konu','yorum','ip','user','books','yorum_puani','id')



class ResimlerAdmin(admin.ModelAdmin):
    list_display = ['books','baslik','image_tag']
    readonly_fields = ('image_tag',)
    
    
    

    
# Register your models here.
admin.site.register(BookCategory)
admin.site.register(Books,BooksAdmin)
admin.site.register(Resimler,ResimlerAdmin)
admin.site.register(Yorumlar,YorumlarAdmin)
