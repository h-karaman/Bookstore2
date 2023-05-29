from django.contrib import admin
from book import models
from mptt.admin import DraggableMPTTAdmin
from book.models import Category, Books, Resimler, Slider, Yorumlar

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    #inlines = [CategoryLangInline]
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Books,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Books,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class BooksResimlerInline(admin.TabularInline):
    model = Resimler
    extra = 3   
    readonly_fields = ('image_tag',)
    
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'status','availability','image_tag']
    list_filter = ['category']
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
    
    
class SliderAdmin(admin.ModelAdmin):
    list_display = ['books','baslik','image_tag']
    readonly_fields = ('image_tag',)

    
# Register your models here.
admin.site.register(Category,CategoryAdmin2)
admin.site.register(Books,BooksAdmin)
admin.site.register(Resimler,ResimlerAdmin)
admin.site.register(Yorumlar,YorumlarAdmin)
admin.site.register(Slider,SliderAdmin)
