from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

def homePageView(request):
    
    return HttpResponse(datetime.date.today(),datetime.datetime.now().time())