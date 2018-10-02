from rest_framework import serializers
from products.models import Product, ProductPrice, GiftCard


class ProductSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Product
		fields = ('id', 'url', 'name', 'code', 'price')

class ProductPriceSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = ProductPrice
		fields = ('id', 'url', 'sale_price', 'sale_date_start', 'sale_date_end')

class GiftCardSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = GiftCard
		fields = ('id', 'url', 'code', 'amount', 'date_start', 'date_end' )
