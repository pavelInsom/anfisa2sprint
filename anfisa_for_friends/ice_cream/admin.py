from django.contrib import admin
from .models import Category

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )

    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )

admin.site.register(IceCream, IceCreamAdmin)