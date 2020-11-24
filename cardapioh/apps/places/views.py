from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .filters import ItemFilter, PlaceFilter, SessionFilter
from .models import Item, Place, Session
from .serializers import ItemModelSerializer, PlaceModelSerializer, SessionModelSerializer


class ItemListAPIView(ModelViewSet):
    queryset = Item.objects.filter(is_active=True).order_by('code')
    serializer_class = ItemModelSerializer
    filter_backends = [SearchFilter, filters.DjangoFilterBackend]
    search_fields = ['name', 'description']
    filterset_class = ItemFilter


class PlaceListAPIView(ModelViewSet):
    queryset = Place.objects.filter(is_active=True).order_by('id')
    serializer_class = PlaceModelSerializer
    filter_backends = [SearchFilter, filters.DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = PlaceFilter


class SessionListAPIView(ModelViewSet):
    queryset = Session.objects.filter(is_active=True).order_by('id')
    serializer_class = SessionModelSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SessionFilter

