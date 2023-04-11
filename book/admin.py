from django.contrib import admin

from book.models import BookCategory, Books

# Register your models here.
admin.site.register(BookCategory)
admin.site.register(Books)
