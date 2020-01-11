from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def homePageView(request):
    
    return HttpResponse(datetime.date.today(),datetime.datetime.now().time())