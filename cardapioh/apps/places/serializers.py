from rest_framework.serializers import ModelSerializer

from .models import Item, Place, Price, Session


class PriceModelSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class ItemModelSerializer(ModelSerializer):
    prices = PriceModelSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'


class SessionModelSerializer(ModelSerializer):
    data = ItemModelSerializer(many=True)

    class Meta:
        model = Session
        fields = '__all__'


class PlaceModelSerializer(ModelSerializer):
    sessions = SessionModelSerializer(many=True)

    class Meta:
        model = Place
        fields = '__all__'
