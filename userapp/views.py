from django.shortcuts import render
from django.http import HttpResponse

def userlogin(request):
    return render(request,"loginuser.html")


# Create your views here.
