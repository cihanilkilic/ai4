from django.contrib import admin
from .models import ProductPackage, StarterPackage, ProfessionalPackage, StandardPackage

@admin.register(ProductPackage)
class ProductPackageAdmin(admin.ModelAdmin):
    list_display = ("package_name", "package_price", "package_duration", "created_at")  # Paket süresi eklendi
    search_fields = ("package_name",)
    list_filter = ("created_at",)


@admin.register(StarterPackage)
class StarterPackageAdmin(admin.ModelAdmin):
    list_display = ("purchased_by", "package_price", "purchase_date", "expiration_date", "is_active")
    search_fields = ("purchased_by__username",)
    list_filter = ("is_active", "purchase_date")

@admin.register(ProfessionalPackage)
class ProfessionalPackageAdmin(admin.ModelAdmin):
    list_display = ("purchased_by", "package_price", "purchase_date", "expiration_date", "is_active")
    search_fields = ("purchased_by__username",)
    list_filter = ("is_active", "purchase_date")

@admin.register(StandardPackage)
class StandardPackageAdmin(admin.ModelAdmin):
    list_display = ("purchased_by", "package_price", "purchase_date", "expiration_date", "is_active")
    search_fields = ("purchased_by__username",)
    list_filter = ("is_active", "purchase_date")