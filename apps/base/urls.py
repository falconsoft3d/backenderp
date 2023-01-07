from django.urls import path
from base.views import StaticHome

urlpatterns = [
    path('', StaticHome.as_view(), name='home'),
]