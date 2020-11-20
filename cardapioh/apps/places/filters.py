from django_filters import rest_framework as filters

from .models import Item, Place, Session


class ItemFilter(filters.FilterSet):
    session = filters.NumberFilter(field_name='session__place__id')

    class Meta:
        model = Item
        fields = ('session',)


class PlaceFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name='user_id')

    class Meta:
        model = Place
        fields = ('user',)


class SessionFilter(filters.FilterSet):
    place = filters.NumberFilter(field_name='place_id')

    class Meta:
        model = Session
        fields = ('place',)

