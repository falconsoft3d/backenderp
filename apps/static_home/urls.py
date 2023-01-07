from django.urls import path
from static_home.views import Home
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
]