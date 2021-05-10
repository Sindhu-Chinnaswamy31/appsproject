from django.urls import path
from myapp import views
urlpatterns = [
    path("carry/<data>",views.carrydata,name="carry"),
    path("<sample>",views.carry),
    path("add/<a>/<b>/<c>",views.add),
    path("sub/<a>/<b>/<c>",views.sub),
    path("fact/<sample>",views.factorial),
    path("fact1/<sample1>",views.fact),
    path("home1/<email>/<password>",views.login),

]
