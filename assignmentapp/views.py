from django.shortcuts import render
from django.http import HttpResponse
#from django.utils import timezone
#from django.utils.timezone import localtime
#from django.conf.urls.defaults import *
import datetime

# Create your views here.

def stdlogin(request,email,password):
    #time = timezone.now()
    # get now datetime based upon django settings.py TZ_INFO
    #time=localtime(now()) 
    time = datetime.datetime.now()   
    return render(request,"stdlogin.html",{"username":email,"pass":password,"time":time})
