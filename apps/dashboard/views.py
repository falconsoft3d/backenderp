from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard/home.html'
    login_url = '/admin/login'
