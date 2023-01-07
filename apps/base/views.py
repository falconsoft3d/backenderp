from django.shortcuts import render

from django.views import generic

class StaticHome(generic.TemplateView):
    template_name = 'base/home.html'
