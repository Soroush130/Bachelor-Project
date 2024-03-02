from django.contrib import admin
from .models import Products, Category, Brand, Gallery, Rate

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Gallery)


class RateAdmin(admin.ModelAdmin):
    list_display = ['product', 'rate']


admin.site.register(Rate, RateAdmin)
