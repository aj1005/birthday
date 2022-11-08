from django.urls import path
from . import views
urlpatterns = [
  path("",views.home,name="home"),
  path("upl",views.upload,name="upl")
  
  
]