from django.contrib import admin

from .models import Item, Place, Session


class ItemTabularInline(admin.StackedInline):
    model = Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'session')
    search_fields = ('name',)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)


class SessionAdmin(admin.ModelAdmin):
    inlines = [ItemTabularInline]
    list_display = ('name', 'place')
    search_fields = ('name',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Session, SessionAdmin)
