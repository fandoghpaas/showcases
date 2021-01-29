import time

from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from store.models import Product
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(['GET'])
def view_products(request):
    response = {}
    start_time = time.time()
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    response['response_time'] = (time.time() - start_time)
    response['from_database'] = True
    response['from_cache'] = False
    response['results'] = results
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_cached_products(request):
    response = {}
    start_time = time.time()
    if 'product' in cache:
        products = cache.get('product')
        response['response_time'] = (time.time() - start_time)
        response['from_database'] = False
        response['from_cache'] = True
        response['results'] = products
        return Response(response, status=status.HTTP_200_OK)
    else:
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        cache.set('product', results, timeout=CACHE_TTL)
        response['response_time'] = (time.time() - start_time)
        response['from_database'] = True
        response['from_cache'] = False
        response['results'] = results
        return Response(response, status=status.HTTP_201_CREATED)
