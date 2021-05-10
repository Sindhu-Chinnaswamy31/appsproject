from django.contrib import admin
from django.urls import path
from userapp import views
userapp = views
userapp  = "USERAPP"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('user',views.userlogin,name='userlogin'),
]