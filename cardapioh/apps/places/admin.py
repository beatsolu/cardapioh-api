from django.contrib import admin
from nested_admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin

from .models import Item, Place, Session, Price
from ..accounts.models import User


class PriceTabularInline(NestedTabularInline):
    model = Price


class ItemStackedInline(NestedStackedInline):
    model = Item
    inlines = [PriceTabularInline]


class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description', 'session')
    search_fields = ('name',)
    inlines = [PriceTabularInline]
    list_editable = ('code',)
    list_display_links = ('name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "session":
            kwargs["queryset"] = Session.objects.filter(place__user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_list_filter(self, request):
        if request.user.is_superuser:
            self.list_filter = ('session', 'session__place')
        return self.list_filter

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(session__place__user=request.user)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_list_filter(self, request):
        if request.user.is_superuser:
            self.list_filter = ('name',)
        return self.list_filter

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class SessionAdmin(NestedModelAdmin):
    inlines = [ItemStackedInline]
    list_display = ('name', 'place', 'position')
    search_fields = ('name',)
    list_editable = ('position',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "place":
            kwargs["queryset"] = Place.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_list_filter(self, request):
        if request.user.is_superuser:
            self.list_filter = ('place',)
        return self.list_filter

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(place__user=request.user)


admin.site.register(Item, ItemAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Session, SessionAdmin)
