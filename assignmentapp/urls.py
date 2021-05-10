from django.urls import path
from assignmentapp import views
urlpatterns = [
    path("stdlogin/<email>/<password>",views.stdlogin,name="stdlogin"),

]