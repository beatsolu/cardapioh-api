from django.contrib import admin

from .models import Item, Place, Session, Price


class PriceTabularInline(admin.StackedInline):
    model = Price


class ItemStackedInline(admin.StackedInline):
    model = Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'session')
    search_fields = ('name',)
    list_filter = ('session', 'session__place')
    inlines = [PriceTabularInline]


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)
    list_filter = ('name',)


class SessionAdmin(admin.ModelAdmin):
    inlines = [ItemStackedInline]
    list_display = ('name', 'place')
    search_fields = ('name',)
    list_filter = ('place',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Session, SessionAdmin)
