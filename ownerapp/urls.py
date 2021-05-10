from django.contrib import admin
from django.urls import path
from ownerapp import views
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('owner',views.ownerapp,name='ownerapp'),
]
