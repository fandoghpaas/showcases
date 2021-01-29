from django.conf.urls import url
from .views import view_products, view_cached_products


urlpatterns = [
    url(r'^$', view_products),
    url(r'^cached/', view_cached_products),
]