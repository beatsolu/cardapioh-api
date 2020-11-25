from django.contrib import admin

from .models import Item, Place, Session, Price


class PriceTabularInline(admin.StackedInline):
    model = Price


class ItemStackedInline(admin.StackedInline):
    model = Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'session')
    search_fields = ('name',)
    inlines = [PriceTabularInline]

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

    def get_list_filter(self, request):
        if request.user.is_superuser:
            self.list_filter = ('name',)
        return self.list_filter

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class SessionAdmin(admin.ModelAdmin):
    inlines = [ItemStackedInline]
    list_display = ('name', 'place')
    search_fields = ('name',)

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
