from django.shortcuts import render
from django.views.generic import TemplateView   # new 2
# Create your views here.

class HomePageView(TemplateView):       # inheritance in TemplateView
    template_name = 'home.html'
