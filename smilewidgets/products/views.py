from django.shortcuts import render, get_object_or_404
from rest_framework import routers, serializers, viewsets
from products.models import Product, ProductPrice, GiftCard
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from datetime import datetime


def get_price(request):
	"""
	Purpose: to get parameters of date and product code and return the appropriate price.
	"""
	productcode = request.GET.get('code')
	date = request.GET.get('date')
	product = Product.objects.get(code=productcode)
	price = ProductPrice.objects.filter(product = product).filter(sale_date_start__lte=datetime.strptime(date, '%Y-%m-%d')).filter(sale_date_end__gte=datetime.strptime(date, '%Y-%m-%d'))
	print("product", product)
	print("price", price)
	if price:
		print("price is true")
		json_result = serializers.serialize('json', price, fields=('sale_price'))
		return HttpResponse(json_result, content_type="application/json")
	else:
		json_result = product.price*.01
		return HttpResponse(json_result, content_type="application/json")
