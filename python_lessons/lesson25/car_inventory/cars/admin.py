from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Car, Dealer


class CarInline(admin.TabularInline):
    model = Car
    extra = 1
    fields = ('brand', 'model', 'year', 'price', 'is_available')
    

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = [CarInline]
    
    
@admin.action(description="Oznacz jako niedostępne")
def mark_as_unavailable(modeladmin, request, queryset):
    updated = queryset.update(is_available=False)
    modeladmin.message_user(
        request, f"Pomyślnie zmieniono status dla {updated} pojazdów.",
        messages.SUCCESS)
    
    
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'brand', 'model', 'year', 'is_available',
                    'image_thumbnail')
    search_fields = ('brand', 'model')
    list_filter = ('is_available', 'year')
    ordering = ('-year', )
    readonly_fields = ('year', )
    actions = [mark_as_unavailable]
    
    @admin.display(description="Pełna nazwa")
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"
    
    @admin.display(description="Miniaturka")
    def image_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "Brak zdjęcia"