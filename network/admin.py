from django.contrib import admin
from .models import NetworkNode, Contacts, Product


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('contacts__city',)
    actions = [clear_debt]

    def city(self, obj):
        return obj.contacts.city if obj.contacts else None

    city.short_description = 'Город'


admin.site.register(NetworkNode, NetworkNodeAdmin)
admin.site.register(Contacts)
admin.site.register(Product)
