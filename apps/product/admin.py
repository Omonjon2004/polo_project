from django.contrib import admin

from apps.product.models import Shoes, Dress


# Register your models here.
@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    pass

@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    pass

