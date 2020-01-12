from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Pages

# Create your views here.

class HomePageView(ListView):
    model = Pages
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

def homePageView(request):
    
    return HttpResponse(datetime.date.today(),datetime.datetime.now().time())