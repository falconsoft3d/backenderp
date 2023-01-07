from django.urls import path
from dashboard.views import Home
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
]