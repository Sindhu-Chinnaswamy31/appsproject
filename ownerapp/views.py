from django.shortcuts import render
from django.http import HttpResponse

def ownerapp(request):
    return render(request,"loginowner.html")

