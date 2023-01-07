from django.shortcuts import render
from django.views import generic

class Home(generic.TemplateView):
    # template_name = 'base/base.html'
    template_name = 'static_home/home.html'

def page_not_found_view(request, exception):
    return render(request, 'base/404.html', status=404)

def contact(request):
    return render(request, 'base/contact.html')

def team(request):
    return render(request, 'base/team.html')