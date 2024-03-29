from django.contrib import admin
from .models import Product,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available','created','updated']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
