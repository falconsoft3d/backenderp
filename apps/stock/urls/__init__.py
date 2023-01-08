from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('product/', include('apps.stock.urls.product')),
]
